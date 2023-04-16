import os
import ast
import pickle
import argparse
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from botsniffer.feature_extraction.feature_extraction import extract_features


def get_features(file_path, tree):
    features = extract_features(file_path, tree)
    feature_values = []
    for key, value in features.items():
        if isinstance(value, str):
            feature_values.append(value)
        elif isinstance(value, list):
            feature_values.extend(value)
        else:
            feature_values.append(str(value))
    sample = ' '.join(feature_values)
    if "ai" in file_path.lower():
        label = True
    else:
        label = False
    return features, sample, label


def generate_trained_data(pkl_path, samples, labels):
    # We will vectorize and train the ML
    # Convert to Numpy
    samples = np.array(samples)
    labels = np.array(labels)
    # Split into different datasets
    X_train, X_test, y_train, y_test = train_test_split(samples, labels, test_size=0.2)
    # Extract features using a CountVectorizer
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)
    # Train a logistic regression classifier on the dataset
    clf = LogisticRegression()
    clf.fit(X_train, y_train)
    # Make predictions on the test set and calculate accuracy
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    # Save the trained model to a file
    with open(pkl_path, "wb") as f:
        pickle.dump(clf, f)


def scan_path(path, identify, train):
    samples = []
    labels = []
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
                        elif train:
                            samples.append(sample)
                            if label:
                                labels.append(1)
                            else:
                                labels.append(0)
                        else:
                            print("Error: you must specify either --identify or --train.")
    else:
        if path.endswith(".py"):
            # Run the feature extraction in a file
            with open(path) as f:
                tree = ast.parse(f.read(), type_comments=True)
                features, sample, label = get_features(path, tree)
                if identify:
                    print(features)
                elif train:
                    samples.append(sample)
                    if label:
                        labels.append(1)
                    else:
                        labels.append(0)
                else:
                    print("Error: you must specify either --identify or --train.")
        else:
            print("Error: '{}' is not a Python source code file.".format(path))
    if train:
        pkl_path = "file.pkl"
        generate_trained_data(pkl_path, samples, labels)


def prepare_training(features, filename):
    if "ai" in file.lower():
        labels.append(1)
    else:
        labels.append(0)

def main():
    parser = argparse.ArgumentParser(description="Scan Python source code files and extract information about functions.")
    parser.add_argument("path", help="The path to scan.")
    parser.add_argument("--identify", action="store_true", help="Identify AI-generated code.")
    parser.add_argument("--train", action="store_true", help="Train a model to identify AI-generated code.")
    args = parser.parse_args()

    scan_path(args.path, args.identify, args.train)


if __name__ == "__main__":
    main()

