#!/bin/bash
#SBATCH --time=23:00:00
#SBATCH -p standard
#SBATCH -n 1
#SBATCH --mem=98000
#SBATCH -A nssac_students
#SBATCH -o simu_bio_2_structure.out
#SBATCH -e simu_bio_2_structure.error

module load anaconda/2019.10-py3.7

python3 main_learn_real_network.py 0 bio2 10
python3 main_learn_real_network.py 0 bio2 100
python3 main_learn_real_network.py 0 bio2 500
python3 main_learn_real_network.py 0 bio2 1000
python3 main_learn_real_network.py 0 bio2 2000
python3 main_learn_real_network.py 0 bio2 3000
python3 main_learn_real_network.py 0 bio2 5000
python3 main_learn_real_network.py 0 bio2 10000
python3 main_learn_real_network.py 0 bio2 50000
python3 main_learn_real_network.py 0 bio2 100000
