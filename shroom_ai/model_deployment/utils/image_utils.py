from PIL import Image
import numpy as np
from config import config

def preprocess_image(image):
    img = Image.open(image).convert('RGB')
    img = img.resize(config.IMAGE_SIZE)
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)