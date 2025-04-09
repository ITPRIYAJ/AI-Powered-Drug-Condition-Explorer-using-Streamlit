from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd

class DrugRecommender:
    def __init__(self, csv_path="data/drug_dataset.csv"):
        self.df = pd.read_csv(csv_path)
        self.vectorizer = CountVectorizer()
        self.model = MultinomialNB()
        self.train()

    def train(self):
        X = self.vectorizer.fit_transform(self.df['Symptoms'])
        y = self.df['DrugName']
        self.model.fit(X, y)

    def predict(self, symptom_text):
        X_input = self.vectorizer.transform([symptom_text])
        return self.model.predict(X_input)[0]
