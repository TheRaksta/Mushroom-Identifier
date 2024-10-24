import os

ORIGINAL_EDIBLE_IMAGES_GCP_BUCKET_NAME = os.environ.get("ORIGINAL_EDIBLE_IMAGES_GCP_BUCKET_NAME")
RESIZED_EDIBLE_IMAGES_GCP_BUCKET_NAME = os.environ.get("RESIZED_EDIBLE_IMAGES_GCP_BUCKET_NAME")
ORIGINAL_KAGGLE_IMAGES_GCP_BUCKET_NAME = os.environ.get("ORIGINAL_KAGGLE_IMAGES_GCP_BUCKET_NAME")
RESIZED_KAGGLE_IMAGES_GCP_BUCKET_NAME = os.environ.get("RESIZED_KAGGLE_IMAGES_GCP_BUCKET_NAME")

RESIZED_KAGGLE_AND_EDIBLE_BUCKET_NAME = os.environ.get("RESIZED_KAGGLE_AND_EDIBLE_BUCKET_NAME")

PIERS_GCP_PROJECT_ID = os.environ.get("PIERS_GCP_PROJECT_ID")
RAKESH_GCP_PROJECT_ID= os.environ.get("RAKESH_GCP_PROJECT_ID")

GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
MUSHROOMS_APPLICATION_CREDENTIALS = os.environ.get("MUSHROOMS_APPLICATION_CREDENTIALS")
