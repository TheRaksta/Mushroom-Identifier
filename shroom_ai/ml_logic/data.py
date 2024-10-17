## Loading and Storing Data
from google.cloud import storage
from shroom_ai.params import PIERS_GCP_BUCKET_NAME
from typing import List

def get_blobs_from_bucket(bucket_name: str) -> List[storage.Blob]:
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs()
    return blobs

if __name__ == "__main__":
    bucket_name = PIERS_GCP_BUCKET_NAME
    blobs = get_blobs_from_bucket(bucket_name)
    for blob in blobs:
        print(blob.name)
