import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import numpy as np

def plot_degree_histograms(data, labels, prefix=""):
    classes = sorted(list(set(labels)))
    num_classes = len(classes)
    labels = np.array(labels)
    
    f, axarr = plt.subplots(num_classes, sharex=True, sharey=True)
    f.suptitle("{}: Average Node Degree Histogram".format(prefix))
    
    for counter, class_category in enumerate(classes):
        idx = np.where(labels == class_category)
        X = data[idx]
        mean_hist = np.mean(np.array(X), axis=0)
        axarr[counter].bar(np.arange(data.shape[1]), mean_hist, label="p: "+class_category)
        
    f.subplots_adjust(hspace=0)
    for ax in axarr:
        ax.label_outer()
        ax.legend()
        
def visualization(data, labels, method="tSNE"):
    if method == "tSNE":
        viz = TSNE(n_components=2, random_state=0)
    elif method == "PCA":
        viz = PCA(n_components=2)
    data_2d = viz.fit_transform(data)
    label_classes = np.unique(labels).tolist()
    
    plt.figure(figsize=(6, 5))
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w', 'orange', 'purple']
    for i, c in zip(label_classes, colors):
        plt.scatter(data_2d[labels == i, 0], data_2d[labels == i, 1], c=c, label=i)
    plt.title("{} visualization of graph classes".format(method))
    plt.legend()
