#!/bin/bash
#SBATCH --job-name=bloom-filter-test
#SBATCH --output=result-%j.out
#SBATCH --error=result-%j.err
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=4GB

module load python/3.8
python3 run_bloom_filter_benchmark.py
