import numpy as np
from PIL import Image
from io import BytesIO
from google.oauth2 import service_account
# from config import config

# def load_images_from_gcs(bucket):
#     blobs = bucket.list_blobs(prefix=config.GCS_IMAGE_PREFIX)
#     images = []
#     labels = []
#     for blob in blobs:
#         if blob.name.lower().endswith(('.jpg', '.jpeg', '.png')):
#             image_data = blob.download_as_bytes()
#             img = Image.open(BytesIO(image_data))
#             img = img.resize(config.IMAGE_SIZE)
#             img_array = np.array(img) / 255.0
#             images.append(img_array)

#             # Extract label from path
#             path_parts = blob.name.split('/')
#             category = path_parts[-2]
#             labels.append(1 if category == 'edible' else 0)

#     return np.array(images), np.array(labels)


### OLD CODE - Not relevant to ML workflow
## Loading and Storing Data
from google.cloud import storage
from io import BytesIO
from PIL import Image
from shroom_ai.params import ORIGINAL_EDIBLE_IMAGES_GCP_BUCKET_NAME, RAKESH_GCP_PROJECT_ID, GOOGLE_APPLICATION_CREDENTIALS
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
    ## returns image data
    return buffer.getvalue()

def upload_resized_images(source_bucket_name: str, dest_bucket_name: str, new_size=(224, 224), format="PNG", upload_content_type="image/png"):
    blobs = get_blobs_from_bucket(source_bucket_name)

    storage_client = storage.Client()
    dest_bucket = storage_client.bucket(dest_bucket_name)

    for blob in blobs:
        image_data = blob.download_as_bytes()
        resized_image_data = resize_image(image_data=image_data, new_size=new_size, format=format)
        new_blob = dest_bucket.blob(blob.name)
        new_blob.upload_from_string(resized_image_data, content_type=upload_content_type)
        print(f'Resized and uploaded: {blob.name} to {dest_bucket_name}')

    print(" Finished uploading all the magic 🍄🍄🍄🍄🍄🍄🍄🍄")

def get_storage_client(project_id: str, credentials=str) -> storage.Client:
    client = storage.Client(project=project_id, credentials=credentials)
    return client

# Will not be committed
if __name__ == "__main__":
    credentials_path = GOOGLE_APPLICATION_CREDENTIALS
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = storage.Client(project=RAKESH_GCP_PROJECT_ID, credentials=credentials)
    bucket_name = ORIGINAL_EDIBLE_IMAGES_GCP_BUCKET_NAME
    blobs = get_blobs_from_bucket(bucket_name)
    for blob in blobs:
        print(blob.name)
        image_data = blob.download_as_bytes()
        print(type(image_data))
        resized_image_data = resize_image(image_data=image_data)
        print("Resized", type(resized_image_data))
        break
