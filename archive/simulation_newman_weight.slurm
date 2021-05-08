#!/bin/bash
#SBATCH --time=23:00:00
#SBATCH -p standard
#SBATCH -n 1
#SBATCH --mem=98000
#SBATCH -A nssac_students
#SBATCH -o simu_newman_weight.out
#SBATCH -e simu_newman_weight.error

module load anaconda/2019.10-py3.7

python3 main_learn_real_network.py 1 newman 10
python3 main_learn_real_network.py 1 newman 100
python3 main_learn_real_network.py 1 newman 500
python3 main_learn_real_network.py 1 newman 1000
python3 main_learn_real_network.py 1 newman 2000
python3 main_learn_real_network.py 1 newman 3000
python3 main_learn_real_network.py 1 newman 5000
python3 main_learn_real_network.py 1 newman 10000
python3 main_learn_real_network.py 1 newman 50000
python3 main_learn_real_network.py 1 newman 100000
