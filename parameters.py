probability_tests = {
    "test1": [0.25, 0.75],
    "test2": [0.49999, 0.50001],
    "test3": [0.495, 0.505],
    "test4": [0.40, 0.45, 0.50, 0.55],
    "test5": [0.48, 0.49, 0.50, 0.51],
    "test6": [0.0, 0.5, 1.0],
    "test7": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
    "test8": [0.45, 0.55],
    "test9": [0.4, 0.6],
    "test10": [0.1, 0.9]
}

graph_types = {
    "fast_gnp_random_graph": 1,
    "watts_strogatz_graph": 2, # rewires existing edge with prob p
    "newman_watts_strogatz_graph": 3, # adds new edge with prob p
    "connected_watts_strogatz_graph": 4, # rewires existing edge with prob p, but ensures connected graph
    "barabasi_albert_graph": 5, # a graph of n nodes is grown by attaching new nodes each with m edges that are preferentially attached to existing nodes with high degree
    "powerlaw_cluster_graph": 6, # growing graphs with powerlaw degree distribution and approximate average clustering
    "random_powerlaw_tree": 7 # returns a tree with a power law degree distribution
}

graph_parameters = {
    "graph_type": graph_types["connected_watts_strogatz_graph"],
    "graphs_per_class": 50,
    "num_nodes": 20, #569 in the Nature study
    "knn": 4, # used in watts-strogatz graphs
    "m_edges": 10, # used in barabasi-albert graph
    "gamma": 3, # used in random powerlaw tree
    "graph_edge_width": 0.1
}