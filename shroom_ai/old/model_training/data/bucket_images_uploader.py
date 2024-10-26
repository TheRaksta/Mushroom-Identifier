## Uploading to gcp buckets
from google.cloud import storage
from google.oauth2 import service_account
from io import BytesIO
import os
from PIL import Image
from typing import List

def get_blobs_from_bucket(client: storage.Client, bucket_name: str) -> List[storage.Blob]:
    bucket = client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    return blobs

def resize_image(image_data, new_size=(224, 224), format="PNG"):
    img = Image.open(BytesIO(image_data))
    img = img.resize(new_size)
    buffer = BytesIO()
    img.save(fp=buffer, format=format)
    ## returns image data
    return buffer.getvalue()

def upload_resized_images(client: storage.Client, source_bucket_name: str, dest_bucket_name: str, new_size=(224, 224), format="PNG", upload_content_type="image/png"):
    blobs = get_blobs_from_bucket(client=client, bucket_name=source_bucket_name)
    dest_bucket = client.bucket(dest_bucket_name)

    for blob in blobs:
        image_data = blob.download_as_bytes()
        resized_image_data = resize_image(image_data=image_data, new_size=new_size, format=format)
        new_blob = dest_bucket.blob(blob.name)
        new_blob.upload_from_string(resized_image_data, content_type=upload_content_type)
        print(f'Resized and uploaded: {blob.name} to {dest_bucket_name}')

    print("Finished uploading all the magic 🍄🍄🍄🍄🍄🍄🍄🍄")

def get_storage_client(project_id: str, credentials_path: str) -> storage.Client:
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    client = storage.Client(project=project_id, credentials=credentials)
    return client

def modify_path_to_be_edible_and_have_no_spaces(original_path):
    directory, filename = os.path.split(original_path)
    directory = directory.replace(" ", "_")
    filename = filename.replace(" ", "_")
    new_directory = os.path.join("edible", directory)
    new_path = os.path.join(new_directory, filename)
    return new_path

def copy_blob_to_new_bucket(client: storage.Client, source_bucket_name, destination_bucket_name):
    """Copies a blob from one bucket to another with a new name."""
    # Get the source bucket and blob
    source_bucket = client.bucket(source_bucket_name)
    destination_bucket = client.bucket(destination_bucket_name)

    blobs = source_bucket.list_blobs()
    for blob in blobs:
        destination_blob = destination_bucket.blob(blob.name)
        destination_blob.rewrite(blob)
        print(f'Resized and uploaded: {blob.name} to {destination_bucket_name}')

    print("Success uploading the mushrooms 🍄🍄🍄🍄🍄🍄🍄🍄")

def copy_blob_to_new_bucket_with_edible_category(source_client: storage.Client, destination_client: storage.Client, source_bucket_name, destination_bucket_name):
    source_bucket = source_client.bucket(source_bucket_name)
    destination_bucket = destination_client.bucket(destination_bucket_name)
    blobs = source_bucket.list_blobs()

    for blob in blobs:
        new_name = modify_path_to_be_edible_and_have_no_spaces(blob.name)
        destination_blob = destination_bucket.blob(new_name)
        image_data = blob.download_as_bytes()
        destination_blob.upload_from_string(image_data, content_type="image/jpeg")
        print(f'Resized and uploaded: {new_name} to {destination_bucket_name}')

    print("Success uploading the mushrooms 🍄🍄🍄🍄🍄🍄🍄🍄")
