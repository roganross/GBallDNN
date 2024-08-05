import os
from PIL import Image
import pillow_heif

def convert_heic_to_jpg(heic_path):
    jpg_path = os.path.splitext(heic_path)[0] + ".jpg"  # Create JPG path with the same name
    heif_file = pillow_heif.read_heif(heic_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(jpg_path, "JPEG")  # Save the converted image as JPEG
    return jpg_path  # Return the path of the saved JPG

def batch_convert_folder(input_folder):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            heic_path = os.path.join(input_folder, filename)
            print(f"Converting: {heic_path}")
            jpg_path = convert_heic_to_jpg(heic_path)  # Convert and get the new JPG path
            os.remove(heic_path)  # Remove the original HEIC file
            print(f"Converted and replaced: {filename} with {os.path.basename(jpg_path)}")

# Example usage
input_folder = r'C:\Users\rogan\Documents\Programming\GBallDNN\GBallSet\0'
batch_convert_folder(input_folder)
