from PIL import Image
import os
import pandas as pd
import numpy as np

def preprocess_image(image_path, target_size=(224, 224)):
    image = Image.open(image_path)
    image = image.resize(target_size)
    # Convert image to numpy array and normalize pixel values
    image = np.array(image) / 255.0  # Normalize to [0, 1]
    return image

def create_label_file(pos_folder, neg_folder, output_file):
    labels = []

    # Positive class (golf ball present)
    for filename in os.listdir(pos_folder):
        if filename.lower().endswith(".jpg"):  # Adjust if using other formats
            labels.append({"filename": filename, "label": 1})

    # Negative class (no golf ball)
    for filename in os.listdir(neg_folder):
        if filename.lower().endswith(".jpg"):  # Adjust if using other formats
            labels.append({"filename": filename, "label": 0})

    df = pd.DataFrame(labels)
    df.to_csv(output_file, index=False)

def save_preprocessed_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".jpg"):  # Adjust if using other formats
            image_path = os.path.join(input_folder, filename)
            preprocessed_image = preprocess_image(image_path)
            output_path = os.path.join(output_folder, filename)
            # Save preprocessed image as JPEG
            Image.fromarray((preprocessed_image * 255).astype(np.uint8)).save(output_path)

# Example usage
pos_folder = r'path\to\folder'
neg_folder = r'path\to\folder'
output_label_file = 'labels.csv'
output_preprocessed_folder = r'path\to\folder'

# Create label file
create_label_file(pos_folder, neg_folder, output_label_file)

# Save preprocessed images to output folder
save_preprocessed_images(pos_folder, os.path.join(output_preprocessed_folder, 'golf_ball'))
save_preprocessed_images(neg_folder, os.path.join(output_preprocessed_folder, 'no_golf_ball'))
