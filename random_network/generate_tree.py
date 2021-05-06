import networkx as nx
import sys
import numpy as np
from scipy import sparse
import numpy as np
from scipy.sparse import diags

n = int(sys.argv[1]) # The number of vertices

G = nx.generators.trees.random_tree(n)

print(nx.info(G))

path = "tree_" + str(n) + ".npz"

A = nx.to_scipy_sparse_matrix(G)

sparse.save_npz(path, A)

