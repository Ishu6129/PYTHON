from PIL import Image
import os

def load_images_from_folder(folder_path):
    image_list = []

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and any(file_path.lower().endswith(extension) for extension in ['.jpg', '.png', '.gif']):
            try:
                image = Image.open(file_path)
                image_list.append(image)
            except Exception as e:
                print(f"Error loading image {file_path}: {e}")

    return image_list


folder_path = r'C:\path\to\your\folder'

image_list = load_images_from_folder(folder_path)


