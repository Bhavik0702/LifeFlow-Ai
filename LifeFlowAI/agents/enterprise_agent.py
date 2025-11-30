import pickle
import os
import pandas as pd
import datetime

class EnterpriseAgent:
    def __init__(self):
        self.model_path = 'LifeFlowAI/models/enterprise_model.pkl'
        self.model = self._load_model()

    def _load_model(self):
        if not os.path.exists(self.model_path):
            print(f"Warning: Model not found at {self.model_path}. Please run training script.")
            return None
        with open(self.model_path, 'rb') as f:
            return pickle.load(f)

    def predict_sales(self, days_ahead=1):
        if not self.model:
            return "Error: Model not loaded."
        
        future_date = datetime.date.today() + datetime.timedelta(days=days_ahead)
        future_ordinal = pd.Timestamp(future_date).toordinal()
        
        prediction = self.model.predict([[future_ordinal]])[0]
        return f"Predicted Sales for {future_date}: {int(prediction)} units"

if __name__ == "__main__":
    agent = EnterpriseAgent()
    print(agent.predict_sales(days_ahead=7))
