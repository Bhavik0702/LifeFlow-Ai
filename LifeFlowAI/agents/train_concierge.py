import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_concierge_model():
    print("Loading data...")
    data_path = 'LifeFlowAI/data/tasks.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    df = pd.read_csv(data_path)
    X = df['Task_Description']
    y = df['Priority']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a pipeline: Vectorizer -> Classifier
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    print("Training model...")
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {acc:.2f}")

    # Save model
    os.makedirs('LifeFlowAI/models', exist_ok=True)
    with open('LifeFlowAI/models/concierge_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved to LifeFlowAI/models/concierge_model.pkl")

if __name__ == "__main__":
    train_concierge_model()
