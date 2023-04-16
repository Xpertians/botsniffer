import os
import ast
import argparse
from botsniffer.feature_extraction.feature_extraction import extract_features


def scan_path(path):
    if not os.path.exists(path):
        print("Error: '{}' does not exist.".format(path))
    elif os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(".py"):
                    file_path = os.path.join(root, file_name)
                    with open(file_path) as f:
                        tree = ast.parse(f.read(), type_comments=True)
                        extract_features(file_path, tree)
    else:
        if path.endswith(".py"):
            with open(path) as f:
                tree = ast.parse(f.read(), type_comments=True)
                extract_features(path, tree)
        else:
            print("Error: '{}' is not a Python source code file.".format(path))

def main():
    parser = argparse.ArgumentParser(description="Scan Python source code files and extract information about functions.")
    parser.add_argument("path", help="The path to scan.")
    args = parser.parse_args()

    scan_path(args.path)

if __name__ == "__main__":
    main()
