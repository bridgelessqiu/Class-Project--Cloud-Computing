import sys
import algorithm.algo as aa
import math
import numpy as np
from scipy import sparse
from scipy.sparse import diags
import networkx as nx

if __name__ == "__main__":
    exp_type = int(sys.argv[1]) # 0: learn the structure, 1: learn the weight
    n = int(sys.argv[2]) # the size of the network
    exponent = int(sys.argv[3]) # this is the exponent of the number of cascades: 1 * 10^{exponnet}
    
    if exp_type == 0:
        # learn_tree_structure(A, p, k, num_of_cascade)
        f = aa.learn_tree_structure
    elif exp_type == 1:
        # learn_tree_weight(A, p, k, num_of_cascade)
        f = aa.learn_tree_weight
    else:
        raise ValueError('Please input 0: learn the structure or 1: learn the weight') 

    path = "random_network/tree_" + str(n) + ".npz"

    A = sparse.load_npz(path)
    p = 0.9
    max_iter = 1000
    num_of_cascade =  10 ** exponent 

    # Run the learning funciton: THIS TAKES A LONG TIME 
    result = f(A, p, max_iter, num_of_cascade)

    if exp_type == 0:
        print("The edge correctness is:{}".format(result))
    else:
        print("The average mean error is:{}".format(result))
