import os
import re
from PIL import Image
base_dir = "./"
def convert_to_webp(file_path):
    try:
        img = Image.open(file_path)
        webp_path = os.path.splitext(file_path)[0] + ".webp"
        img.save(webp_path, "WEBP")
        print(f"Converted {file_path} to {webp_path}")
    except Exception as e:
        print(f"Failed to convert {file_path}: {e}")
        
def convert_to_snake_case(file_name):
    snake_case_name = re.sub(r'[\s-]+', '_', file_name)
    snake_case_name = re.sub(r'[^\w\._]', '', snake_case_name)
    return snake_case_name.lower()


directories = [
  ...
]


supported_extensions = [".jpg", ".jpeg", ".png", ".nef", ".webp"]
for directory in directories:
    dir_path = os.path.join(base_dir, directory)
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.splitext(file_name)[1].lower() in supported_extensions:
    
            snake_case_name = convert_to_snake_case(file_name)
            new_file_path = os.path.join(dir_path, snake_case_name)

    
            if new_file_path != file_path:
                os.rename(file_path, new_file_path)
                file_path = new_file_path

    
            convert_to_webp(file_path)
