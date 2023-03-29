import argparse
import json
import os

# Make sure cwd is project root
os.chdir(os.path.join(os.path.dirname(__file__), os.pardir))

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--problem_id", default=0, type=int)
parser.add_argument("-p", "--code_path", default="outputs/codes/", type=str)

args = parser.parse_args()

problem_id = args.problem_id
code_path = os.path.join(args.code_path, f"{problem_id}.json")

with open(code_path, 'r') as f:
    data = json.load(f)

data = data[str(problem_id)]
prompt = data['prompt']
codes = data['code']

print("###  Prompt  ###")
print(prompt)

for (index, code) in enumerate(codes):
    print(f"###  Sample {index + 1}  ###\n")
    print(code)
