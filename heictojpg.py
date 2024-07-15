import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(heic_path, jpg_path):
    heif_file = pillow_heif.read_heif(heic_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(jpg_path, "JPEG")

def batch_convert_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            jpg_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
            print(f"Converting: {heic_path} to {jpg_path}")
            convert_heic_to_jpg(heic_path, jpg_path)
            print(f"Converted: {filename}")

# Example usage
input_folder = r'C:\Users\rogan\Documents\Programming\GBallDNN\GBallSet\1'
output_folder = r'C:\Users\rogan\Documents\Programming\GBallDNN\GBallSet\1j'

batch_convert_folder(input_folder, output_folder)
