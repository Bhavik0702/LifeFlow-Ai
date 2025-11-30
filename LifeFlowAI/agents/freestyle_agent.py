import random

class FreestyleAgent:
    def __init__(self):
        self.generator = None
        self._load_model()

    def _load_model(self):
        print("Loading Freestyle Agent (Creative Mode)...")
        try:
            from transformers import pipeline
            # 'distilgpt2' is a lightweight version of GPT-2, perfect for local CPU usage.
            # Explicitly use PyTorch ('pt') to avoid TensorFlow DLL issues on some Windows systems
            self.generator = pipeline('text-generation', model='distilgpt2', framework='pt')
            print("Freestyle Agent loaded with DistilGPT-2 (Real LLM).")
        except ImportError as e:
            print(f"CRITICAL ERROR: Deep Learning libraries not found. ({e})")
            print("Please run: pip install transformers torch")
            self.generator = None
        except Exception as e:
            print(f"Error loading model: {e}")
            self.generator = None

    def generate_content(self, prompt):
        if self.generator:
            try:
                # Generate text with tuned parameters to prevent repetition
                result = self.generator(
                    prompt, 
                    max_new_tokens=100,       # Use max_new_tokens instead of max_length
                    num_return_sequences=1,
                    do_sample=True,
                    top_k=50,
                    top_p=0.95,
                    temperature=0.7,          # Lower temperature for more coherent text
                    repetition_penalty=1.2,   # Slightly lower penalty to avoid garbage
                    no_repeat_ngram_size=2,
                    pad_token_id=50256,       # Explicitly set pad_token_id to eos_token_id
                    truncation=True           # Explicitly enable truncation
                )
                return result[0]['generated_text']
            except Exception as e:
                return f"Error during generation: {e}"
        else:
            return "Error: The AI model is not loaded. Please ensure 'transformers' and 'torch' are installed."

if __name__ == "__main__":
    agent = FreestyleAgent()
    print(agent.generate_content("The future of AI is"))
