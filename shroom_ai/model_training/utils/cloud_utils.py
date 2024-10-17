from google.cloud import storage
import os
from config import config

def connect_to_gcs():
    try:
        client = storage.Client(project=config.GCS_PROJECT_ID)
        return client
    except Exception as e:
        print(f"Error connecting to Google Cloud Storage: {e}")
        return None

def get_bucket(client):
    try:
        bucket = client.get_bucket(config.GCS_BUCKET_NAME)
        return bucket
    except Exception as e:
        print(f"Error accessing bucket {config.GCS_BUCKET_NAME}: {e}")
        return None