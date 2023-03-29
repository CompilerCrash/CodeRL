import argparse
import os
import pickle

# Make sure cwd is project root
os.chdir(os.path.join(os.path.dirname(__file__), os.pardir))

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--problem_id", default=1, type=int)
parser.add_argument("-p", "--dataset_path", default="data/APPS/train/", type=str)
parser.add_argument('--gt_solutions', action='store_true')
parser.add_argument('--binary_prediction', action='store_true')

args = parser.parse_args()

problem_id = args.problem_id
gt_solutions = args.gt_solutions
critic_scores_path = os.path.join(args.dataset_path, f"{problem_id:04d}",
                                  "solutions_critic_scores.pkl" if gt_solutions else "gen_solutions_critic_scores.pkl")
binary_prediction = args.binary_prediction

if binary_prediction:
    result_map = {0: "not passed tests", 1: "passed tests"}
else:
    result_map = {0: "compile error", 1: "runtime error", 2: "failed tests", 3: "passed tests"}

with open(critic_scores_path, 'rb') as f:
    data = pickle.load(f)

gt_error_types = data['gt_error_type']
pred_error_types = data['pred_error_type']

for (index, (gt_error_type, pred_error_type)) in enumerate(zip(gt_error_types, pred_error_types)):
    print(f"\n###  Sample {index + 1}  ###\n")

    print(f"True      error type: {gt_error_type} ({result_map[gt_error_type]})")
    print(f"Predicted error type: {pred_error_type} ({result_map[pred_error_type]})")
