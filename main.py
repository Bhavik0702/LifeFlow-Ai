import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from LifeFlowAI.agents.concierge_agent import ConciergeAgent
from LifeFlowAI.agents.enterprise_agent import EnterpriseAgent
from LifeFlowAI.agents.good_agent import AgentsForGood
from LifeFlowAI.agents.freestyle_agent import FreestyleAgent

def main():
    print("\n==================================================")
    print("       Welcome to LifeFlow AI - Unified Ecosystem")
    print("==================================================")
    print("Initializing Intelligent Agents... Please wait.")
    
    concierge = ConciergeAgent()
    enterprise = EnterpriseAgent()
    good_agent = AgentsForGood()
    freestyle = FreestyleAgent()
    
    print("\n[SYSTEM] All Agents Online.")
    
    while True:
        print("\n--------------------------------------------------")
        print("Select an Agent to interact with:")
        print("1. Concierge Agent (Productivity & Task AI)")
        print("2. Agents for Good (Community Vision AI)")
        print("3. Enterprise Agent (Business Forecasting AI)")
        print("4. Freestyle Agent (Creative GenAI)")
        print("5. Exit System")
        print("--------------------------------------------------")
        
        choice = input("\nYour Choice (1-5): ")
        
        if choice == '1':
            print("\n[Concierge Agent] Hello! I can help prioritize your tasks.")
            task = input(">> Describe your task: ")
            priority = concierge.prioritize_task(task)
            print(f"\n[Analysis] Based on my training, this task is: {priority} Priority")
            
        elif choice == '2':
            print("\n[Agents for Good] I am ready to analyze infrastructure images.")
            img_path = input(">> Enter image path (or press Enter to run a simulation): ")
            if not img_path:
                # Create a dummy file for testing
                with open("test_image.jpg", "w") as f: f.write("dummy")
                img_path = "test_image.jpg"
                result = good_agent.report_issue(img_path)
                os.remove("test_image.jpg")
            else:
                result = good_agent.report_issue(img_path)
            print(f"\n[Report] {result}")
            
        elif choice == '3':
            print("\n[Enterprise Agent] I can forecast future sales trends.")
            days = input(">> How many days ahead should I predict? (default 1): ")
            days = int(days) if days.isdigit() else 1
            prediction = enterprise.predict_sales(days)
            print(f"\n[Forecast] {prediction}")
            
        elif choice == '4':
            print("\n[Freestyle Agent] I am your creative partner. Give me a prompt!")
            prompt = input(">> Prompt: ")
            print("\n[Thinking] Generating creative content... (this may take a moment)")
            idea = freestyle.generate_content(prompt)
            print(f"\n[Generated Output]:\n{idea}")
            
        elif choice == '5':
            print("\n[SYSTEM] Shutting down LifeFlow AI. Goodbye!")
            break
        else:
            print("\n[Error] Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
