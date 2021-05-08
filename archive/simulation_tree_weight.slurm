#!/bin/bash
#SBATCH --time=23:00:00
#SBATCH -p standard
#SBATCH -n 1
#SBATCH --mem=98000
#SBATCH -A nssac_students
#SBATCH -o simu_tree_weight.out
#SBATCH -e simu_tree_weight.error

module load anaconda/2019.10-py3.7

python3 main_learn_tree.py 1 1000 10
python3 main_learn_tree.py 1 1000 100
python3 main_learn_tree.py 1 1000 500
python3 main_learn_tree.py 1 1000 1000
python3 main_learn_tree.py 1 1000 2000
python3 main_learn_tree.py 1 1000 3000
python3 main_learn_tree.py 1 1000 5000
python3 main_learn_tree.py 1 1000 10000
python3 main_learn_tree.py 1 1000 50000
python3 main_learn_tree.py 1 1000 100000
