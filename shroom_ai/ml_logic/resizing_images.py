import os
from google.cloud import storage
from PIL import Image
import io
import json
from google.oauth2 import service_account

# this pulls in the credentials from the json file correctly

with open(os.environ.get('GOOGLE_APPLICATION_CREDENTIAL')) as source:
        info = json.load(source)

storage_credentials = service_account.Credentials.from_service_account_info(info)

client = storage.Client(project=os.environ.get('GCP_PROJECT_ID'), credentials=storage_credentials)

# client = storage.Client(project=os.environ.get('GCP_PROJECT_ID'),credentials=os.environ.get("GOOGLE_APPLICATION_CREDENTIAL"))

original_bucket_name = 'edible_mushroom_images'
resized_bucket_name = 'edible_mushroom_images_resized_224_224'

TARGET_SIZE = (224, 224)

# Function to resize an image
def resize_image(image_content):
    image = Image.open(io.BytesIO(image_content))
    image = image.convert('RGB')  # Ensure the image is in RGB format
    image = image.resize(TARGET_SIZE, Image.ANTIALIAS)
    output = io.BytesIO()
    image.save(output, format="JPEG")
    output.seek(0)
    return output

# Process images in the original bucket and save to the resized bucket

def process_images_in_buckets():
    # Access the original and resized buckets
    original_bucket = client.bucket(original_bucket_name)
    resized_bucket = client.bucket(resized_bucket_name)

    # List all blobs (images) in the original bucket
    blobs = original_bucket.list_blobs()

    for blob in blobs:
        # Only process JPEG images
        if blob.name.lower().endswith(('.jpeg', '.jpg')):
            print(f"Processing image: {blob.name}")

            # Download the original image
            image_data = blob.download_as_bytes()

            # Resize the image
            resized_image = resize_image(image_data)

            # Create the new blob name, keeping the same folder structure
            new_blob_name = blob.name  # Keep the same path and name

            # Upload the resized image to the resized bucket
            new_blob = resized_bucket.blob(new_blob_name)
            new_blob.upload_from_file(resized_image, content_type='image/jpeg')
            print(f"Image {blob.name} resized and uploaded to {new_blob_name}")

if __name__ == "__main__":
    process_images_in_buckets()
