import datetime
import os
from config import config

def train_model(model, X_train, y_train, X_val, y_val):
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=config.EPOCHS,
        batch_size=config.BATCH_SIZE,
    )
    return history

def save_model_to_gcs(model, bucket):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    model_name = f"mushroom_model_{timestamp}.h5"
    
    model_path = os.path.join(config.GCS_MODEL_PREFIX, model_name)
    
    # Save model locally first
    model.save(model_name)
    
    # Upload to GCS
    blob = bucket.blob(model_path)
    blob.upload_from_filename(model_name)
    
    # Remove local file
    os.remove(model_name)
    
    print(f"Model saved to gs://{bucket.name}/{model_path}")