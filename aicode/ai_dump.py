import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# load data
data = pd.read_csv('source_code.csv')

# preprocess data
data['source_code'] = data['source_code'].str.replace('\n', '')
data['source_code'] = data['source_code'].str.replace('\t', '')
data['source_code'] = data['source_code'].str.replace('\r', '')

# create features
vectorizer = TfidfVectorizer(ngram_range=(1, 3), stop_words='english')
features = vectorizer.fit_transform(data['source_code'])

# train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(features, data['label'])

# predict labels
test_code = '''
def function_name(parameter1, parameter2):
    for i in range(10):
        if i % 2 == 0:
            print(i)
'''
test_features = vectorizer.transform([test_code])
predicted_label = model.predict(test_features)

print(predicted_label)
