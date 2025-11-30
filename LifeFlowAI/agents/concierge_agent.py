import pickle
import os

class ConciergeAgent:
    def __init__(self):
        self.model_path = 'LifeFlowAI/models/concierge_model.pkl'
        self.model = self._load_model()

    def _load_model(self):
        if not os.path.exists(self.model_path):
            print(f"Warning: Model not found at {self.model_path}. Please run training script.")
            return None
        with open(self.model_path, 'rb') as f:
            return pickle.load(f)

    def prioritize_task(self, task_description):
        if not self.model:
            return "Error: Model not loaded."
        prediction = self.model.predict([task_description])[0]
        return prediction

if __name__ == "__main__":
    agent = ConciergeAgent()
    print(f"Task: 'Buy milk' -> Priority: {agent.prioritize_task('Buy milk')}")
    print(f"Task: 'Submit annual report' -> Priority: {agent.prioritize_task('Submit annual report')}")
