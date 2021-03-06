import sys
import time
import algorithm.algo as aa
import math
import numpy as np
from scipy import sparse
from scipy.sparse import diags
import networkx as nx

if __name__ == "__main__":
    exp_type = int(sys.argv[1]) # 0: learn the structure, 1: learn the weight
    n = int(sys.argv[2]) # the size of the network
    num_of_cascade = int(sys.argv[3]) # the number of cascades

    path = "random_network/degree_bounded/gnp_" + str(n) + ".npz"
    A = sparse.load_npz(path)
    max_d = 15
    p = 0.15
    max_iter = 1000

    # The starting processing time
    start = time.time()

    if exp_type == 0:
        # learn_degree_bounded_structure(A, p, k, max_d, num_of_cascade)
        result = aa.learn_degree_bounded_structure(A, p, max_iter, max_d, num_of_cascade)
    elif exp_type == 1:
        # learn_degree_bounded_weight(A, p, k, num_of_cascade)
        result = aa.learn_degree_bounded_weight(A, p, max_iter, num_of_cascade)
    else:
        raise ValueError('Please input 0: learn the structure or 1: learn the weight') 

    # The ending processing time
    end = time.time()

    print("The time in seconds for degree bounded graph of size {} with {} cascades is: {} s".format(n, num_of_cascade, round(end-start, 3)))

    if exp_type == 0:
        print("The edge correctness is:{}".format(round(result, 5)))
    else:
        print("The average mean error is:{}".format(round(result, 5)))
