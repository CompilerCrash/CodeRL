import json

problem_id = 0  # change this line as needed
code_path = f"outputs/codes/{problem_id}.json"

with open(code_path, 'r') as f:
    data = json.load(f)[str(problem_id)]
    prompt = data['prompt']
    codes = data['code']

    print("###  Prompt  ###")
    print(prompt)

    for (index, code) in enumerate(codes):
        print(f"###  Sample {index + 1}  ###\n")
        print(code)
