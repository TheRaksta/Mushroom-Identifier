import os
import random
from google.cloud import storage
import json
from google.oauth2 import service_account

with open(os.environ.get('GOOGLE_APPLICATION_CREDENTIAL')) as source:
        info = json.load(source)

storage_credentials = service_account.Credentials.from_service_account_info(info)


with open(os.environ.get('PIERS_GOOGLE_APPLICATION_CREDENTIAL')) as source:
        info = json.load(source)

storage_credentials_piers = service_account.Credentials.from_service_account_info(info)

# Initialize the Cloud Storage client
client = storage.Client(project=os.environ.get('GCP_PROJECT_ID'),credentials=storage_credentials)

client_piers= storage.Client(project=os.environ.get('PIERS_GCP_PROJECT_ID'),credentials=storage_credentials_piers)

# Define source and destination buckets
source_bucket_name = os.environ.get('PIERS_BUCKET')
destination_bucket_name = os.environ.get('BUCKET_NAME_RESIZE')
percentage_to_copy = 0.7  # 70%

# Get the source and destination buckets
source_bucket = client_piers.bucket(source_bucket_name)
destination_bucket = client.bucket(destination_bucket_name)

# List the top-level folders to process
folders_to_process = ['edible', 'conditionally_edible', 'deadly', 'poisonous']

def list_files(bucket, prefix=''):
    """List all files in a bucket with a specific prefix."""
    blobs = bucket.list_blobs(prefix=prefix)
    return [blob.name for blob in blobs]

def copy_file(blob_name, source_bucket, destination_bucket):
    """Copy a file from the source bucket to the destination bucket."""
    source_blob = source_bucket.blob(blob_name)
    destination_blob = destination_bucket.blob(blob_name)

    # Copy the file
    destination_blob.rewrite(source_blob)
    print(f'Copied {blob_name} to {destination_bucket_name}')

# Process each folder in 'folders_to_process'
for folder in folders_to_process:
    print(f"Processing folder: {folder}")

    # List all files in the current folder
    all_files = list_files(source_bucket, prefix=folder + "/")

    # Group files by subfolders within this folder
    subfolder_files = {}

    for file in all_files:
        # Ignore the folder itself, only consider files
        if not file.endswith('/'):
            # Extract the subfolder path (adjust based on folder depth if needed)
            subfolder = '/'.join(file.split('/')[:-1])
            if subfolder not in subfolder_files:
                subfolder_files[subfolder] = []
            subfolder_files[subfolder].append(file)

    # Process each subfolder
    for subfolder, files in subfolder_files.items():
        if folder == 'edible':
            # Copy only 70% of files from each subfolder under 'edible'
            num_files_to_copy = int(len(files) * percentage_to_copy)
            files_to_copy = random.sample(files, num_files_to_copy)
        else:
            # Copy all files from other folders
            files_to_copy = files

        # Copy the selected files
        for file in files_to_copy:
            copy_file(file, source_bucket, destination_bucket)

print('File copying complete!')
