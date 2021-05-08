import networkx as nx
import sys
import numpy as np
from scipy import sparse
import numpy as np
from scipy.sparse import diags

n = int(sys.argv[1]) # The number of vertices
p = float(sys.argv[2]) # The probability of edge creation

G = nx.generators.random_graphs.fast_gnp_random_graph(n, p)

print(nx.info(G))

path = "degree_bounded/gnp_" + str(n) + ".npz"

A = nx.to_scipy_sparse_matrix(G)

sparse.save_npz(path, A)

