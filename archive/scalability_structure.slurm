#!/bin/bash
#SBATCH --time=23:00:00
#SBATCH -p standard
#SBATCH -n 1
#SBATCH --mem=98000
#SBATCH -A nssac_students
#SBATCH -o simu_scala_structure_new.out
#SBATCH -e simu_scala_structure_new.error

module load anaconda/2019.10-py3.7

python3 main_learn_tree.py 0 500 10
python3 main_learn_tree.py 0 1000 10
python3 main_learn_tree.py 0 1500 10
python3 main_learn_tree.py 0 2000 10
python3 main_learn_tree.py 0 2500 10
python3 main_learn_tree.py 0 3000 10
python3 main_learn_tree.py 0 3500 10
python3 main_learn_tree.py 0 4000 10
python3 main_learn_tree.py 0 4500 10
python3 main_learn_tree.py 0 5000 10
python3 main_learn_tree.py 0 5500 10
python3 main_learn_tree.py 0 6000 10
python3 main_learn_tree.py 0 6500 10
python3 main_learn_tree.py 0 7000 10
python3 main_learn_tree.py 0 7500 10
python3 main_learn_tree.py 0 8000 10
python3 main_learn_tree.py 0 8500 10
python3 main_learn_tree.py 0 9000 10
python3 main_learn_tree.py 0 9500 10
python3 main_learn_tree.py 0 10000 10
