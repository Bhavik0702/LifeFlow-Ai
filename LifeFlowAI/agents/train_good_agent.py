import os
# import tensorflow as tf
# from tensorflow.keras.preprocessing.image import ImageDataGenerator

def train_good_agent_model():
    data_dir = 'LifeFlowAI/data/dataset_good'
    
    # Check if data exists
    if not os.path.exists(data_dir) or not os.listdir(data_dir):
        print("Data directory empty. Please add images to 'LifeFlowAI/data/dataset_good' to train the CNN.")
        return

    print("Initializing CNN training...")
    # Code to train CNN would go here:
    # 1. Setup ImageDataGenerator
    # 2. Build CNN Model (Conv2D -> MaxPool -> Flatten -> Dense)
    # 3. Compile and Fit
    # 4. Save model to LifeFlowAI/models/good_agent_cnn.h5
    
    print("Training skipped: No images found. (This is expected for the initial setup)")

if __name__ == "__main__":
    train_good_agent_model()
