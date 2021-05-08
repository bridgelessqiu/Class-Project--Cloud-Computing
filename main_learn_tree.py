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
    num_of_cascade = int(sys.argv[3]) # The number of cascades
    
    if exp_type == 0:
        # learn_tree_structure(A, p, k, num_of_cascade)
        f = aa.learn_tree_structure
    elif exp_type == 1:
        # learn_tree_weight(A, p, k, num_of_cascade)
        f = aa.learn_tree_weight
    else:
        raise ValueError('Please input 0: learn the structure or 1: learn the weight') 

    path = "random_network/tree/tree_" + str(n) + ".npz"

    A = sparse.load_npz(path)
    p = 0.9
    max_iter = 1000

    # The starting processing time
    start = time.process_time()

    # Run the learning funciton: THIS TAKES A LONG TIME 
    result = f(A, p, max_iter, num_of_cascade)

    # The ending processing time
    end = time.process_time()

    print("The time in seconds for tree of size {} with {} cascades is: {} s".format(n, num_of_cascade, round(end-start, 3)))

    if exp_type == 0:
        print("The edge correctness is:{}".format(round(result, 5)))
    else:
        print("The average mean error is:{}".format(round(result, 5)))
