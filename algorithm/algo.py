import numpy as np
import math
import random
from scipy import sparse
import networkx as nx

# -------------------- #
#       Cascase        #
# -------------------- #
def cascade(A, v_time, v_state, p, k):
    """
    Description
    -----------
    This function computes the cascade of the infection where the dynamic
    is specified as shown in the paper.

    Parameters
    ----------
    A: n x n scipy sparse matrix
        The adjacency matrix of the graph

    p: float (0, 1)
        The default transmission probability

    v_time: n x 1 numpy vector
        The initial infection time of each vertex

    v_state: n x 1 numpy vector
        The initial infection state of each vertex

    k: integer > 0
        The maximum number of iterations

    Output
    ------
    v_time: n x 1 numpy array
        The vector that consists of the infection time of each vertex
    v_state: n x 1 numpy array
        The vector that consists of the infection state of each vertex
    """
    
    # The number of vertices
    n = np.shape(A)[0]

    # The one and zero vectors
    one = np.ones((n, 1), dtype = 'float')
    zero = np.zeros((n, 1), dtype = 'float')

    # The infected vector: b_2
    b_2 = v_state

    # The recovery vector: b_3
    b_3 = np.zeros((n, 1), dtype = 'float') # No one is recovered at day 1

    # The susceptible vector: b_4
    b_4 = -b_2 - b_3
    b_4[b_4 == 0.0] = 1.0
    b_4[b_4 < 0.0] = 0.0

    for day in range(2, k): # Note that at day 0, only one vertex is infected which is given as a problem input
        b_4_last = b_4 
        b_2_last = b_2

        # The # of infected neighbors of each v
        d = A @ b_2_last

        # Compute the newly infected nodes
        temp = np.full((n, 1), 1.0 - p)
        q = np.power(temp, d)
        q = np.multiply(b_4_last, one - q)

        # Has to flatten q to pass it to the binomial funciton
        q_f = q.flatten()
        # Compute newly infected nodes
        newly_infected = np.reshape(np.random.binomial(1, q_f), (-1 ,1))

        # Recovery
        b_3 = b_2_last + b_3 # update b_3, as shown in the paper, each infected vertex recover in exactly one time step

        # Update b_2
        b_2 = newly_infected

        # Update the susceptible vector
        b_4 = -b_2 - b_3
        b_4[b_4 == 0.0] = 1.0
        b_4[b_4 < 0.0] = 0.0

        # Update v_state
        v_state = v_state + newly_infected
        v_time = v_time + newly_infected * day

        # A fixed point is reached under zero infection
        if np.array_equal(b_2, zero):
            return v_state, v_time

    print("the maximum number of iterations is reached")
    return v_state, v_time

# ------------------------------------------------------ #
#       Learn the structure of bidirectional tree        #
# ------------------------------------------------------ #
def learn_tree_structure(A, p, k, num_of_cascade):
    """
    Description
    -----------
    This algorithm recovers the structures of trees under the extreme noise setting. For deails, please see the paper

    Parameters
    ----------
    A: The adjacency matrix of the graph
    p: The default transmission probability
    k: The maximum number of days (iterations) for each cascade
    num_of_cascades: The number of cascades to run

    Output
    -------
    The algorithm returns the edge correctness.
    """

    n = np.shape(A)[0]
    H = {} # As suggested in the paper, this is the fraction of cascades for which both i and j were infected
    
    # Initilize all to 0
    for i in range(n):
        for j in range(n):
            H[(i, j)] = 0
    
    # Run MANY cascades
    for _ in range(num_of_cascade):
        infected = random.randint(0, n-1) # Initially only one infected vertex
        v_state = np.zeros((n, 1), dtype = 'float') # Initially only one infected vertex
        v_state[infected, 0] = 1 
        v_time = v_state # The infection time is 1

        v_state, v_time = cascade(A, v_time, v_state, p, k) # run the cascade
       
        for i in range(n - 1):
            for j in range(i + 1, n):
                if v_state[i] == v_state[j] == 1:
                    H[(i, j)] += 1
    
    # Sort H in descending order
    sorted_H = dict(sorted(H.items(), key=lambda item: item[1],  reverse = True))
    
    # Avoid forming cycles
    selected = [0] * n
    edges = []
    total = 0
    for key, value in sorted_H.items():
        if total != n:
            u = key[0]
            v = key[1]
            if (selected[u] == 0) or (selected[v] == 0):
                edges.append((u, v))
                selected[u] = 1
                selected[v] = 1
            total += 1
        else:
            break
    
    offset = 2 # This is needed to correctly compute EC
    # Compute EC
    num_of_correct_edges = 0
    A_dense = sparse.csr_matrix.todense(A)
    for e in edges:
        u = e[0]
        v = e[1]
        if A[u, v] == 1:
            num_of_correct_edges += 1

    EC = float(offset * num_of_correct_edges / (n-1))

    return EC


# ---------------------------------------------------- #
#       Learn the weights of bidirectional tree        #
# ---------------------------------------------------- #
def learn_tree_weight(A, p, k, num_of_cascade):
    """
    Description
    -----------
    This algorithm recovers the weights of trees. For deails, please see the paper

    Parameters
    ----------
    A: The adjacency matrix of the graph
    p: The default transmission probability
    k: The maximum number of days (iterations) for each cascade
    num_of_cascades: The number of cascades to run

    Output
    ------
    The algorithm returns the mean absolute error
    """
    n = np.shape(A)[0]
    H = {} # The fraction of cascades for which i and j both infection, and i reported before j
    J = [0] * n # The fraction of infection for which i got infected  

    # Initilize all to 0
    for i in range(n):
        for j in range(n):
            H[(i, j)] = 0

    # Run MANY cascades
    for _ in range(num_of_cascade):
        infected = random.randint(0, n-1) # Initially only one infected vertex
        v_state = np.zeros((n, 1), dtype = 'float') # Initially only one infected vertex
        v_state[infected, 0] = 1
        v_time = v_state

        v_state, v_time = cascade(A, v_time, v_state, p, k) # run the cascade
        
        for i in range(n):
            if v_state[i] == 1:
                J[i] += float(1 / num_of_cascade)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if (v_state[i] == v_state[j] == 1) and (v_time[i] < v_time[j]):
                    H[(i, j)] += float(1 / num_of_cascade)
                elif (v_state[i] == v_state[j] == 1) and (v_time[i] > v_time[j]):
                    H[(j, i)] += float(1 / num_of_cascade)
   
    # The predicted weight
    predicted_p = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            if (J[i] * (0.025) + H[(i, j)] * 0.5 - H[(j, i)] * 0.5) != 0:
                predicted_p[i, j] = float((H[(i, j)] * 0.5 - H[(j, i)] * 0.5) / (J[i] * (0.025) + H[(i, j)] * 0.5 - H[(j, i)] * 0.5))
   

    A_dense = sparse.csr_matrix.todense(A)

    sum = 0
    # Compute the mean absolute error
    for i in range(n-1):
        for j in range(i + 1, n):
            if A_dense[i, j] == 1:
                sum += abs(float(predicted_p[i, j] - p))
            
    mae = float(sum / (n - 1))

    return mae


# ----------------------------------------------------------------- #
#           Learn the structure of the degree bounded graph         #
# ----------------------------------------------------------------- #
def learn_degree_bounded_structure(A, p, k, max_d, num_of_cascade):
    """
    Description
    -----------
    This algorithm recovers the structure of degree-bounded graphs

    Parameters
    ----------
    A: The adjacency matrix of the graph
    p: The default transmission probability
    k: The maximum number of days (iterations) for each cascade
    max_d: The maximum degree of the graph
    num_of_cascades: The number of cascades to run

    Output
    -------
    The algorithm returns the edge correctness
    """
    n = np.shape(A)[0]
    H = {} 

    # Initilize all to 0
    for i in range(n):
        for j in range(n):
            H[(i, j)] = 0

    # Run MANY cascades
    for _ in range(num_of_cascade):
        infected = random.randint(0, n-1) # Initially only one infected vertex
        v_state = np.zeros((n, 1), dtype = 'float') # Initially only one infected vertex
        v_state[infected, 0] = 1
        v_time = v_state

        v_state, v_time = cascade(A, v_time, v_state, p, k) # run the cascade

        for i in range(n - 1):
            for j in range(i + 1, n):
                if v_state[i] == v_state[j] == 1:
                    H[(i, j)] += 1

        # Sort H in descending order
        sorted_H = dict(sorted(H.items(), key=lambda item: item[1],  reverse = True))

    # Avoid adding too many edges which violates the maximum degree
    degree = [0] * n
    edges = []
    for key, value in sorted_H.items():
        u = key[0]
        v = key[1]
        if (degree[v] < max_d) and (degree[v] < max_d):
            edges.append((u, v))
            degree[u] += 1
            degree[v] += 1
    
    # Compute EC
    offset = 2
    num_of_correct_edges = 0
    A_dense = sparse.csr_matrix.todense(A)
    for e in edges:
        u = e[0]
        v = e[1]
        if A[u, v] == 1:
            num_of_correct_edges += 1

    EC = float(offset * num_of_correct_edges /(10 * (n-1))) # the average degree is 10

    return EC

# ------------------------------------------------------------ #
#        Learn the weights of the degree bounded graph         #
# ------------------------------------------------------------ #
def learn_degree_bounded_weight(A, p, k, num_of_cascade):
    """
    Description
    -----------
    This algorithm recovers the weights of degree bounded graph

    Parameters
    -----------
    A: The adjacency matrix of the graph
    p: The default transmission probability
    k: The maximum number of days (iterations) for each cascade
    num_of_cascades: The number of cascades to run

    Output
    -------
    The algorithm returns mean absolte errors
    """
    n = np.shape(A)[0]
    nc = num_of_cascade
    F = {} # Defined in the paper
    H = {} # Defined in the paper
    J = [0] * n # The fraction of infection for which i got infected

    # Initilize all to 0
    for i in range(n):
        for j in range(n):
            F[(i, j)] = 0
            H[(i, j)] = 0

    # Run MANY cascades
    for _ in range(num_of_cascade):
        infected = random.randint(0, n-1) # Initially only one infected vertex
        v_state = np.zeros((n, 1), dtype = 'float') # Initially only one infected vertex
        v_state[infected, 0] = 1
        v_time = v_state

        v_state, v_time = cascade(A, v_time, v_state, p, k) # run the cascade

        for i in range(n):
            if v_state[i] == 1:
                J[i] += float(1 / num_of_cascade)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if v_state[i] == v_state[j] == 1:
                    F[(i, j)] += float(1 / num_of_cascade)
                    F[(j, i)] += float(1 / num_of_cascade)
                    if v_time[i] > v_time[j]:
                        H[(i, j)] += float(1 / num_of_cascade)
                    elif v_time[i] > v_time[j]:
                        H[(j, i)] += float(1 / num_of_cascade)
    
    predicted_p = np.zeros((n, n))
    
    # Defined in the paper
    for i in range(n):
        for j in range(n):
            V_ij = V_ji = 0
            if (H[(i, j)] ** 2 + n * J[i] * J[j]) != 0:
                V_ij = (F[(i, j)] ** 2) / (H[(i, j)] ** 2 + n * J[i] * J[j])
            if (H[(j, i)] ** 2 + n * J[i] * J[j]) != 0:
                V_ji = (F[(j, i)] ** 2) / (H[(j, i)] ** 2 + n * J[i] * J[j])

            delta = 0.025 - 4 * (V_ij * 0.5 - V_ji * 0.5) * 0.5 *  (V_ij - V_ji)
            if (0.025 + math.sqrt(delta)) != 0:
                predicted_p[i, j] = float((V_ji - V_ij) / (0.025 + math.sqrt(delta)))

    A_dense = sparse.csr_matrix.todense(A)
    sum = 0
    offset = 2
    # Compute the mean absolute error
    for i in range(n-1):
        for j in range(i + 1, n):
            if A_dense[i, j] == 1:
                sum += abs(float(predicted_p[i, j] - p))

    mae = float(offset * sum / (n * math.log(nc))) # this needs to be changed
    return mae
