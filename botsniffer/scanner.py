import os
import ast
import pickle
import argparse

from botsniffer.feature_extraction.feature_extraction import extract_features
from botsniffer.ml_model.model import train_model, predict


def get_features(file_path, tree):
    features = extract_features(file_path, tree)
    feature_values = []
    for key, value in features.items():
        if isinstance(value, str):
            feature_values.append(float(value))
        elif isinstance(value, list):
            feature_values.extend(value)
        else:
            feature_values.append(float(value))
    sample = feature_values
    # For training, is expected that AI generated
    # files had "ai" in their name/path
    if "ai" in file_path.lower():
        label = True
    else:
        label = False
    return features, sample, label


def scan_path(path, identify, train):
    is_ai = False
    samples = []
    labels = []
    pkl_path = "botsniffer/data/botcode.pkl"
    if not os.path.exists(path):
        print("Error: '{}' does not exist.".format(path))
    elif os.path.isdir(path):
        # Run the feature extraction in a folder
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(".py"):
                    file_path = os.path.join(root, file_name)
                    with open(file_path) as f:
                        tree = ast.parse(f.read(), type_comments=True)
                        features, sample, label = get_features(file_path, tree)
                        if identify:
                            print(features)
                            is_ai = predict(pkl_path, features)
                        elif train:
                            samples.append(sample)
                            if label:
                                labels.append(1)
                            else:
                                labels.append(0)
                        else:
                            print("Error: you must specify \
                            either --identify or --train.")
    else:
        if path.endswith(".py"):
            # Run the feature extraction in a single file
            with open(path) as f:
                tree = ast.parse(f.read(), type_comments=True)
                features, sample, label = get_features(path, tree)
                if identify:
                    print(features)
                    is_ai = predict(pkl_path, features)
                elif train:
                    samples.append(sample)
                    if label:
                        labels.append(1)
                    else:
                        labels.append(0)
                else:
                    print("Error: you must specify either \
                    --identify or --train.")
        else:
            print("Error: '{}' is not a Python source code file.".format(path))
    if train:
        train_model(pkl_path, labels, samples)
        print('Trained:')
        print(' - labels:', len(labels))
        print(' - samples:', len(samples))
    elif identify:
        print('File:', path)
        print('AI:', is_ai)
    else:
        print("Error: you must specify either \
        --identify or --train.")


def main():
    parser = argparse.ArgumentParser(
        description="Scan Python source code files \
        and extract information about functions.")
    parser.add_argument("path", help="The path to scan.")
    parser.add_argument(
        "--identify",
        action="store_true",
        help="Identify AI-generated code.")
    parser.add_argument(
        "--train",
        action="store_true",
        help="Train a model to identify AI-generated code.")
    args = parser.parse_args()

    scan_path(args.path, args.identify, args.train)


if __name__ == "__main__":
    main()
