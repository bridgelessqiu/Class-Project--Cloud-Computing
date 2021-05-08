#!/bin/bash
#SBATCH --time=23:00:00
#SBATCH -p standard
#SBATCH -n 1
#SBATCH --mem=98000
#SBATCH -A nssac_students
#SBATCH -o simu_scala_weight_new.out
#SBATCH -e simu_scala_weight_new.error

module load anaconda/2019.10-py3.7

python3 main_learn_tree.py 1 500 10
python3 main_learn_tree.py 1 1000 10
python3 main_learn_tree.py 1 1500 10
python3 main_learn_tree.py 1 2000 10
python3 main_learn_tree.py 1 2500 10
python3 main_learn_tree.py 1 3000 10
python3 main_learn_tree.py 1 3500 10
python3 main_learn_tree.py 1 4000 10
python3 main_learn_tree.py 1 4500 10
python3 main_learn_tree.py 1 5000 10
python3 main_learn_tree.py 1 5500 10
python3 main_learn_tree.py 1 6000 10
python3 main_learn_tree.py 1 6500 10
python3 main_learn_tree.py 1 7000 10
python3 main_learn_tree.py 1 7500 10
python3 main_learn_tree.py 1 8000 10
python3 main_learn_tree.py 1 8500 10
python3 main_learn_tree.py 1 9000 10
python3 main_learn_tree.py 1 9500 10
python3 main_learn_tree.py 1 10000 10
