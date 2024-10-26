from google.cloud import storage
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

def get_latest_model_blob(bucket):
    blobs = bucket.list_blobs(prefix=config.GCS_MODEL_PREFIX)
    model_blobs = [blob for blob in blobs if blob.name.endswith('.h5')]
    if not model_blobs:
        return None
    return max(model_blobs, key=lambda x: x.updated)