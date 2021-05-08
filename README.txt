Required packages (all available in Rivanna):
1. networkx
2. numpy
3. scipy
4. matplotlib

--------------------------------------------------------

The project consists of the following directorys and files:

1. DIR:algorithm
    *FILE:algo.py - Contains the implementations of the cascade and the proposed algorithms

2. DIR:random_network
    *DIR:degree_bounded 
        - Contains the npz files for degree bounded random graphs

    *DIR:tree 
        - Contains the npz files for random trees

    *PROGRAM:generate_gnp.py 
        - Generates random degree-bounded graphs.

        Two command line arguments:
            a). size of the network
            b). probability of edge creation

        Note: All the random graphs have been generated. There is no need to regenerate them.

    *PROGRAM:generate_tree.py
        - Generates random trees. 

        One command line argument:
            a). size of the network

        Note: All the random graphs have been generated. There is no need to regenerate them.

3. DIR:real_network
    *DIR: bio / bio2 / econ / erdos / fb / google / newman / retweet / retweet2 / router / social
        - Contains the npz files for real-world networks

        Note: All the npz files have been generated. There is no need to regenerate them.

4. PROGRAM:main_learn_gnp.py
    - Run the algorithms on learning structures / weights of degree-bounded random graphs
    
    Three command line arguments:
        a). Indicator for the classes of learning tasks - 0: learn structures; 1: learn weights
        b). Size of the network to learn (1000, 2000, ..., 10000)
        c). Number of cascades (To see immediate results, do not set it to high like 100. 10 cascades takes roughly less than a minute)

    Example:
        python3 main_learn_gnp.py 1 1000 10

5. PROGRAM:main_learn_tree.py
    - Run the algorithms on learning structures / weights of random trees

    Three command line arguments:
        a). Indicator for the classes of learning tasks - 0: learn structures; 1: learn weights
        b). Size of the network to learn (1000, 2000, ..., 10000)
        c). Number of cascades (To see immediate results, do not set it to high like 100. 10 cascades takes roughly less than a minute)

    Example:
        python3 main_learn_tree.py 1 1000 10

6. PROGRMA:main_learn_real_network.py
    - Run the algorithms on learning structures / weights of real-world networks

    Three command line arguments:
        a). Indicator for the classes of learning tasks - 0: learn structures; 1: learn weights
        b). Name of the network: bio2, newman, etc
        c). Number of cascades (To see immediate results, do not set it to high like 100. 10 cascades takes roughly less than a minute)

    Example:
        python3 main_learn_real_network.py 0 newman 10
