import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

def train_model(X, y):
    # Initialize the machine learning model
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)

    # Train the model on the input data
    model.fit(X, y)

    # Save the trained model to disk
    joblib.dump(model, "model.joblib")

def load_model():
    # Load the trained model from disk
    model = joblib.load("model.joblib")
    return model

def predict(X):
    # Load the trained model from disk
    model = load_model()

    # Make a prediction on the input data
    prediction = model.predict(X)

    return prediction[0]
