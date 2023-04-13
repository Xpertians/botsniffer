import numpy as np
import pytest
from ai_detector.ml_model.model import train_model, predict

@pytest.fixture(scope="module")
def data():
    X = np.array([[0.5, 0.2, 0.8, 0.4, 0.6],
                  [0.1, 0.9, 0.2, 0.8, 0.7],
                  [0.3, 0.4, 0.1, 0.5, 0.9],
                  [0.7, 0.6, 0.4, 0.2, 0.1]])
    y = np.array([0, 1, 0, 1])
    return X, y

def test_train_model(data):
    X, y = data
    train_model(X, y)
    # Assert that the model is not None after training
    assert predict(X[0].reshape(1, -1)) is not None

def test_predict(data):
    X, y = data
    train_model(X, y)
    # Assert that the model correctly predicts the labels of the training data
    assert predict(X[0].reshape(1, -1)) == y[0]
    assert predict(X[1].reshape(1, -1)) == y[1]
    assert predict(X[2].reshape(1, -1)) == y[2]
    assert predict(X[3].reshape(1, -1)) == y[3]
