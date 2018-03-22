import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def print_results(predictions, labels, name):
    print("{}: {}".format(name, (predictions == labels).sum() / float(len(labels))))

def pad_zeros(input_vector, output_size):
    pad = np.zeros(output_size - input_vector.shape[0])
    return np.append(input_vector, pad)

def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def graph_to_degree_hist(G):
    degree_hist = np.array(nx.degree_histogram(G))
    degree_hist_padded = pad_zeros(degree_hist, nx.number_of_nodes(G))
    return degree_hist_padded

def generate_graph(num_nodes, p, k=None, m=None, gamma=3, graph_type=1):
    if graph_type == 1:
        G = nx.fast_gnp_random_graph(n=num_nodes, p=p)
    elif graph_type == 2:
        G = nx.watts_strogatz_graph(n=num_nodes, k=k, p=p)
    elif graph_type == 3:
        G = nx.newman_watts_strogatz_graph(n=num_nodes, k=k, p=p)
    elif graph_type == 4:
        G = nx.connected_watts_strogatz_graph(n=num_nodes, k=k, p=p)
    elif graph_type == 5:
        G = nx.barabasi_albert_graph(n=num_nodes, m=m)
    elif graph_type == 6:
        G = nx.powerlaw_cluster_graph(n=num_nodes, m=m, p=p)
    elif graph_type == 7:
        G = nx.random_powerlaw_tree(n=num_nodes, gamma=gamma)
    return G

def generate_dataset(probs_list, graph_params, draw_sample=True):
    graphs_train = []
    labels_train = []
    graphs_test = []
    labels_test = []

    graph_type = graph_params["graph_type"]
    graphs_per_class = graph_params["graphs_per_class"]
    num_nodes = graph_params["num_nodes"]
    knn = graph_params["knn"]
    m_edges = graph_params["m_edges"]
    gamma = graph_params["gamma"]
    graph_edge_width = graph_params["graph_edge_width"]
    
    for class_type, prob in enumerate(probs_list):
        for i in range(graphs_per_class):
            G_train = generate_graph(num_nodes, prob, knn, m_edges, gamma, graph_type=graph_type)
            G_test = generate_graph(num_nodes, prob, knn, m_edges, gamma, graph_type=graph_type)
            graphs_train.append(G_train)
            graphs_test.append(G_test)
            labels_train.append(str(prob))
            labels_test.append(str(prob))
        if draw_sample:
            plt.figure(class_type)
            nx.draw_circular(G_train, with_labels=True, font_weight='bold', width=graph_edge_width)
            # nx.draw_spring(G_train, with_labels=True, font_weight='bold', width=graph_edge_width)
            # print("rewiring probability: {} | cc: {} | sp {}".format(prob, cc.average_clustering(G_train),sp.average_shortest_path_length(G_train)))
    return graphs_train, labels_train, graphs_test, labels_test

