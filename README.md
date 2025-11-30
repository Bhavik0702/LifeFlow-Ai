<<<<<<< HEAD
# LifeFlow-Ai
=======
# LifeFlow AI: A Unified Agent Ecosystem

**LifeFlow AI** is a multi-agent machine learning system designed to automate daily tasks, support communities, enhance business workflows, and encourage creative experimentation.

## 🤖 The Agents

This project features four specialized agents, each powered by a distinct AI model:

1.  **Concierge Agent (Productivity)**
    *   **Function:** Prioritizes your daily to-do list.
    *   **Tech:** Naive Bayes Text Classifier (Scikit-Learn).
    *   **Capability:** Classifies tasks as High, Medium, or Low priority based on urgency.

2.  **Enterprise Agent (Business)**
    *   **Function:** Forecasts inventory and sales trends.
    *   **Tech:** Linear Regression (Scikit-Learn).
    *   **Capability:** Predicts future sales counts to help with resource planning.

3.  **Agents for Good (Community)**
    *   **Function:** Identifies infrastructure issues (potholes, garbage) from images.
    *   **Tech:** Convolutional Neural Network (CNN) Framework.
    *   **Capability:** Automated issue reporting system (Simulation Mode).

4.  **Freestyle Agent (Creativity)**
    *   **Function:** Generates creative content and ideas.
    *   **Tech:** DistilGPT-2 Transformer (HuggingFace & PyTorch).
    *   **Capability:** A real local Large Language Model (LLM) for text generation.

## 📂 Project Structure

*   `LifeFlowAI/agents/`: Source code for all agent logic.
*   `LifeFlowAI/data/`: Synthetic datasets used for training.
*   `LifeFlowAI/models/`: Saved model artifacts.
*   `main.py`: A CLI tool to interact with the ecosystem.
*   `LifeFlowAI_Demo.ipynb`: A Jupyter Notebook demonstrating the agents.

## 🚀 How to Run

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Run the CLI:**
    ```bash
    python main.py
    ```
3.  **Explore the Notebook:**
    Open `LifeFlowAI_Demo.ipynb` to see the agents in action visually.

## 📊 Dataset Info
The project includes synthetic datasets generated for demonstration:
*   `tasks.csv`: 1000+ labeled tasks for the Concierge Agent.
*   `sales_data.csv`: 1 year of simulated sales history for the Enterprise Agent.

---
*Built for the Kaggle Capstone Project.*
>>>>>>> 4dd7015 (Initial commit: LifeFlow AI project)
