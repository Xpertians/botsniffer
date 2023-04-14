import os
import ast
import argparse
from feature_extraction.feature_extraction import extract_features


def get_functions(file_path):
    with open(file_path) as f:
        tree = ast.parse(f.read(), type_comments=True)
        extract_features(file_path, tree)
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append({
                    "name": node.name,
                    "lineno": node.lineno
                })
        return functions

def scan_path(path):
    if not os.path.exists(path):
        print("Error: '{}' does not exist.".format(path))
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(".py"):
                    file_path = os.path.join(root, file_name)
                    functions = get_functions(file_path)
                    print("File: {}".format(file_path))
                    for function in functions:
                        print("- Function '{}' defined at line {}".format(
                            function["name"], function["lineno"]))
    else:
        if path.endswith(".py"):
            functions = get_functions(path)
            print("File: {}".format(path))
            for function in functions:
                print("- Function '{}' defined at line {}".format(
                    function["name"], function["lineno"]))
        else:
            print("Error: '{}' is not a Python source code file.".format(path))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan Python source code files and extract information about functions.")
    parser.add_argument("path", help="The path to scan.")
    args = parser.parse_args()

    scan_path(args.path)
