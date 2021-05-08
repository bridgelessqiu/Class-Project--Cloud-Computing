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
    network_name = str(sys.argv[2]) # newman, bio2, retweet, retweet_2, social
    num_of_cascade = int(sys.argv[3]) # the number of cascades

    path = "real_network/" + network_name + "/" + network_name + ".npz"
    A = sparse.load_npz(path)
    n = np.shape(A)[0]
    max_d = 5
    p = 0.15
    correction = 2
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

    print("The time in seconds for real network of size {} with {} cascades is: {} s".format(n, num_of_cascade, round(end-start, 3)))

    if exp_type == 0:
        print("The edge correctness is:{}".format(round(result, 5)))
    else:
        print("The average mean error is:{}".format(round(correction * result, 5)))
