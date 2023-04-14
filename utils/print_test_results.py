import argparse
import os
import pickle
import sys

# Make sure cwd is project root
root_path = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir))
os.chdir(root_path)
sys.path.extend([root_path])

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--problem_id", default=0, type=int)
parser.add_argument("-p", "--test_result_path", default="outputs/test_results/", type=str)
parser.add_argument('--print_codes', action='store_true')

args = parser.parse_args()

problem_id = args.problem_id
test_result_path = os.path.join(args.test_result_path, f"{problem_id}.pkl")
print_codes = args.print_codes

result_map = {-2: "compile error", -1: "runtime error", False: "failed tests", True: "passed tests"}

with open(test_result_path, 'rb') as f:
    data = pickle.load(f)

data = data[problem_id]
codes = data['sols']
errors = data['errors']
results = data['results']

for (index, (code, error, result)) in enumerate(zip(codes, errors, results)):
    error = error[0]
    result = result[0]

    print(f"###  Sample {index + 1}  ###\n")

    if print_codes:
        print(code)

    if error is None:
        print("Error: None")
    else:
        error_msg = error[0]
        error_trace = error[1]
        print(f"Error:\n{error_msg}")
        for s in error_trace:
            print(s)

    print(f"Result: {result} ({result_map[result]})\n")
