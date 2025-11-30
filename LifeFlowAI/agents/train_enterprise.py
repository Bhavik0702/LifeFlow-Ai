import pandas as pd
import pickle
import os
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def train_enterprise_model():
    print("Loading sales data...")
    data_path = 'LifeFlowAI/data/sales_data.csv'
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found.")
        return

    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Feature Engineering: Convert date to ordinal for regression
    df['Date_Ordinal'] = df['Date'].map(pd.Timestamp.toordinal)
    
    X = df[['Date_Ordinal']]
    y = df['Sales']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training Linear Regression model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Model MSE: {mse:.2f}")

    # Save model
    os.makedirs('LifeFlowAI/models', exist_ok=True)
    with open('LifeFlowAI/models/enterprise_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    print("Model saved to LifeFlowAI/models/enterprise_model.pkl")

if __name__ == "__main__":
    train_enterprise_model()
