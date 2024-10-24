import numpy as np
from PIL import Image
from io import BytesIO
from config import config

def load_images_from_gcs(bucket):
    blobs = bucket.list_blobs(prefix=config.GCS_IMAGE_PREFIX)
    images = []
    labels = []
    for blob in blobs:
        if blob.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            image_data = blob.download_as_bytes()
            img = Image.open(BytesIO(image_data))
            img = img.resize(config.IMAGE_SIZE)
            img_array = np.array(img) / 255.0
            images.append(img_array)

            # Extract label from path
            path_parts = blob.name.split('/')
            category = path_parts[-2]
            labels.append(1 if category == 'edible' else 0)

    return np.array(images), np.array(labels)
