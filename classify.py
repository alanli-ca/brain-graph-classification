from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.dummy import DummyClassifier
from sklearn.model_selection import GridSearchCV

classifiers = {
    "svm": SVC(),
    "random_forest": RandomForestClassifier(),
    "gradient_boosting": GradientBoostingClassifier(),
    "ada_boost": AdaBoostClassifier(),
    "knn": KNeighborsClassifier(),
    "gnb": GaussianNB(),
    "dummy": DummyClassifier()
}

parameters_search = {
    "svm": {'kernel':['rbf'], 'C':[0.1, 1, 5, 10]},
    "random_forest": {'n_estimators': [10, 20, 50, 100], 'criterion': ['gini', 'entropy'], 'max_features': ["auto", "log2"]},
    # "gradient_boosting": ,
    # "ada_boost": ,
    "knn": {'n_neighbors': [5, 10, 20]},
    # "gnb": ,
    "dummy": {'strategy': ["stratified", "most_frequent"]}
}
