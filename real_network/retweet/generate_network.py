import networkx as nx
import numpy as np
from scipy import sparse

G = nx.read_edgelist("retweet_g1.edges")

print(nx.info(G))

path_1 = "retweet.npz"

A_1 = nx.to_scipy_sparse_matrix(G)

sparse.save_npz(path_1, A_1)

