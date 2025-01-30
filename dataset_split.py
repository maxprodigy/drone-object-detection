# -*- coding: utf-8 -*-

# Step 1: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Step 2: Navigate to the dataset directory
import os
dataset_path = '/content/drive/MyDrive/drone-object-detection'
os.chdir(dataset_path)

# Step 3: Install required libraries
!pip install opencv-python matplotlib split-folders

# Step 4: Split the dataset
import splitfolders

input_folder = 'images'  # Folder containing all images
output_folder = 'split_dataset'  # Folder to save the split dataset

splitfolders.ratio(input_folder, output=output_folder, seed=42, ratio=(0.8, 0.2))

# Step 5: Verify the split
train_folder = os.path.join(output_folder, 'train')
test_folder = os.path.join(output_folder, 'test')

print(f"Train images: {len(os.listdir(train_folder))}")
print(f"Test images: {len(os.listdir(test_folder))}")

# Step 6: Save the split dataset to Google Drive (optional)
!cp -r /content/split_dataset /content/drive/MyDrive/drone-object-detection/
