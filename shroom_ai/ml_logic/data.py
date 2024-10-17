## Loading and Storing Data
from google.cloud import storage
from io import BytesIO
from PIL import Image
from shroom_ai.params import ORIGINAL_KAGGLE_IMAGES_GCP_BUCKET_NAME
from typing import List

def get_blobs_from_bucket(bucket_name: str) -> List[storage.Blob]:
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    return blobs

def resize_image(image_data, new_size=(224, 224), format="PNG"):
    img = Image.open(BytesIO(image_data))
    img = img.resize(new_size)
    buffer = BytesIO()
    img.save(fp=buffer, format=format)
    return buffer.getvalue()




## Will not be committed
if __name__ == "__main__":
    bucket_name = ORIGINAL_KAGGLE_IMAGES_GCP_BUCKET_NAME
    blobs = get_blobs_from_bucket(bucket_name)
    for blob in blobs:
        print(blob.name)
        image_data = blob.download_as_bytes()
        print(type(image_data))
        resized_image_data = resize_image(image_data=image_data)
        print("Resized", type(resized_image_data))
        break
