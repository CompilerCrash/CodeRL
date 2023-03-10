import pickle

problem_id = 0  # change this line as needed
test_result_path = f"../outputs/test_results/{problem_id}.pkl"
print_codes = False

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
