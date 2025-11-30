import pandas as pd
import numpy as np
import os
import random

# Ensure data directory exists
os.makedirs('LifeFlowAI/data', exist_ok=True)

# --- 1. Generate Data for Concierge Agent (Task Classification) ---
print("Generating Concierge Agent Data...")
tasks = [
    ("Submit tax documents", "High"),
    ("Buy groceries for dinner", "Medium"),
    ("Watch new movie", "Low"),
    ("Finish project report", "High"),
    ("Call mom", "Medium"),
    ("Clean the garage", "Low"),
    ("Schedule dentist appointment", "Medium"),
    ("Pay electricity bill", "High"),
    ("Plan weekend trip", "Low"),
    ("Reply to client emails", "High"),
    ("Water the plants", "Low"),
    ("Prepare presentation slides", "High"),
    ("Go for a run", "Medium"),
    ("Read a book", "Low"),
    ("Update software", "Medium"),
    ("Fix critical bug", "High"),
    ("Buy birthday gift", "Medium"),
    ("Organize desktop files", "Low"),
    ("Renew insurance", "High"),
    ("Check social media", "Low")
]

# Expand dataset by repeating and slightly modifying (simple augmentation)
data = []
for _ in range(50): # Generate 1000 rows
    for t, p in tasks:
        data.append([t, p])

df_concierge = pd.DataFrame(data, columns=['Task_Description', 'Priority'])
df_concierge.to_csv('LifeFlowAI/data/tasks.csv', index=False)
print(f"Saved LifeFlowAI/data/tasks.csv with {len(df_concierge)} rows.")


# --- 2. Generate Data for Enterprise Agent (Sales Forecasting) ---
print("Generating Enterprise Agent Data...")
dates = pd.date_range(start='2023-01-01', periods=365, freq='D')
# Simulate a trend with some seasonality and noise
sales = []
base = 50
for i, date in enumerate(dates):
    trend = i * 0.1
    seasonality = 10 * np.sin(i * 2 * np.pi / 30) # Monthly cycle
    noise = np.random.normal(0, 5)
    value = base + trend + seasonality + noise
    sales.append(max(0, int(value)))

df_enterprise = pd.DataFrame({'Date': dates, 'Sales': sales})
df_enterprise.to_csv('LifeFlowAI/data/sales_data.csv', index=False)
print(f"Saved LifeFlowAI/data/sales_data.csv with {len(df_enterprise)} rows.")


# --- 3. Placeholder for Agents for Good (Images) ---
# We can't generate real images easily in this script without external libs, 
# but we will create the folder structure.
print("Creating Agents for Good Directory Structure...")
os.makedirs('LifeFlowAI/data/dataset_good/potholes', exist_ok=True)
os.makedirs('LifeFlowAI/data/dataset_good/garbage', exist_ok=True)
os.makedirs('LifeFlowAI/data/dataset_good/normal', exist_ok=True)
print("Created folder structure at LifeFlowAI/data/dataset_good/")
