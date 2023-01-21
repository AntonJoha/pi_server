import os
import random

from PIL import Image
from get_inky import get_inky


def random_image():
    file_names = os.listdir("img")
    file_count = len(file_names)
    pos = random.randint(0, file_count -1)
    
    file_path = "img/" + file_names[pos]
    return Image.open(file_path).convert("RGB")

random_image()
