# This script transforms the test result data (incl. the generated solutions) into the format that the
# generate_critic_scores(_binary) and train_critic(_deepspeed) scripts expect and saves it into the folders of the
# respective problems.

# Reads:
# ${test_result_path}/????.pkl
# Conditionally writes (depending on --baseline_solutions):
# ${dataset_path}/????/{gen_solutions.json, baseline_solutions.json}

import argparse
import json
import os
import pickle
import sys

# Make sure cwd is project root
root_path = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
os.chdir(root_path)
sys.path.extend([root_path])

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--start", default=0, type=int)
parser.add_argument("-e", "--end", default=10000, type=int)
parser.add_argument("-t", "--test_result_path", default="outputs/test_results/", type=str)
parser.add_argument("-d", "--dataset_path", default="data/APPS/train/", type=str)
parser.add_argument('--baseline_solutions', action='store_true')

args = parser.parse_args()

start = args.start
end = args.end
test_result_path = args.test_result_path
dataset_path = args.dataset_path
baseline_solutions = args.baseline_solutions

for problem_id in range(start, end):
    source_file = os.path.join(test_result_path, f"{problem_id}.pkl")
    destination_file = os.path.join(dataset_path, f"{problem_id:04d}",
                                    "baseline_solutions.json" if baseline_solutions else "gen_solutions.json")

    if not os.path.isfile(source_file):
        print(f"{source_file} does not exist")
        continue

    with open(source_file, 'rb') as f:
        data_in = pickle.load(f)

    data_in = data_in[problem_id]
    results = data_in['results']
    codes = data_in['sols']
    # we drop 'errors' since we don't need it to generate critic scores (and it's not JSON serializable anyway)

    data_out = [{'result': result[0], 'code': code} for (result, code) in zip(results, codes)]

    if baseline_solutions and len(data_out) > 1:
        print(f"{source_file} contains {len(data_out)} samples but only 1 is needed as baseline; dropping the others")
        data_out = [data_out[0]]

    with open(destination_file, 'w') as f:
        json.dump(data_out, f)
