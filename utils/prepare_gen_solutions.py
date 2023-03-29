# This script transforms the test result data (incl. the generated solutions) into the format that the
# generate_critic_scores and generate_critic_scores_binary scripts expect and saves it into the folders of the
# respective problems.

# Reads:
# ${test_result_path}/????.pkl
# Writes:
# ${dataset_path}/????/gen_solutions.json

import argparse
import json
import os
import pickle

# Make sure cwd is project root
os.chdir(os.path.join(os.path.dirname(__file__), os.pardir))

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--start", default=0, type=int)
parser.add_argument("-e", "--end", default=10000, type=int)
parser.add_argument("-t", "--test_result_path", default="outputs/test_results/", type=str)
parser.add_argument("-d", "--dataset_path", default="data/APPS/train/", type=str)

args = parser.parse_args()

start = args.start
end = args.end
test_result_path = args.test_result_path
dataset_path = args.dataset_path

for problem_id in range(start, end):
    source_file = os.path.join(test_result_path, f"{problem_id}.pkl")
    destination_file = os.path.join(dataset_path, f"{problem_id:04d}", "gen_solutions.json")

    if not os.path.isfile(source_file):
        print(f"{source_file} does not exist")
        continue

    with open(source_file, 'rb') as f:
        data_in = pickle.load(f)

    data_in = data_in[problem_id]
    results = data_in['results']
    codes = data_in['sols']
    # we can drop 'errors' since we don't need it to generate critic scores (and it's not JSON serializable)

    data_out = [{'result': result[0], 'code': code} for (result, code) in zip(results, codes)]

    with open(destination_file, 'w') as f:
        json.dump(data_out, f)
