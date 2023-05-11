# Quickly load and inspect file contents from your Python console. Use `from console_utils import *`.

import json
import os
import pickle
import pprint
import sys

codes = "outputs/codes/"
test_results = "outputs/test_results/"
apps_train = "data/APPS/train/"
apps_test = "data/APPS/test/"


def load(path: str, also_print=True) -> str | list[any] | dict[any] | None:
    if not os.path.isfile(path):
        print(f"{path} does not exist", file=sys.stderr)
        data = None
    elif path.endswith(".txt"):
        with open(path, 'r') as f:
            data = f.read()
    elif path.endswith(".json"):
        with open(path, 'r') as f:
            data = json.load(f)
    elif path.endswith(".pkl"):
        with open(path, 'rb') as f:
            data = pickle.load(f)
    else:
        print(f"Don't know how to open {path}", file=sys.stderr)
        data = None

    if also_print and data is not None:
        pprint.pprint(data)

    return data
