import tensorflow as tf
from utils.cloud_utils import get_latest_model_blob
import tempfile
import os

def load_latest_model(bucket):
    latest_model_blob = get_latest_model_blob(bucket)
    if latest_model_blob is None:
        raise ValueError("No model found in the specified GCS bucket")

    with tempfile.NamedTemporaryFile(delete=False) as temp_model_file:
        latest_model_blob.download_to_filename(temp_model_file.name)
        model = tf.keras.models.load_model(temp_model_file.name)
    
    os.unlink(temp_model_file.name)
    return model