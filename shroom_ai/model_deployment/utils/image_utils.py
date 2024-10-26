from PIL import Image
import numpy as np
from model_deployment.config.config import IMAGE_SIZE

def preprocess_image(image):
    img = Image.open(image).convert('RGB')
    img = img.resize(IMAGE_SIZE)
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)
