from config import config
from data import data_loader, data_processor
from models import model_builder, model_trainer
from utils import cloud_utils, performance_utils
from sklearn.model_selection import train_test_split

def main():
    # Connect to Google Cloud Storage
    client = cloud_utils.connect_to_gcs()
    if client is None:
        return
    
    bucket = cloud_utils.get_bucket(client)
    if bucket is None:
        return
    
    # Load and process data
    images, labels = data_loader.load_images_from_gcs(bucket)
    X, y = data_processor.preprocess_data(images, labels)
    
    # Split data
    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=config.TEST_SPLIT, stratify=y, random_state=config.RANDOM_SEED
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=config.VALIDATION_SPLIT, 
        stratify=y_train_val, random_state=config.RANDOM_SEED
    )
    
    # Build and train model
    model = model_builder.build_model()
    history = model_trainer.train_model(model, X_train, y_train, X_val, y_val)
    
    # Save model
    model_trainer.save_model_to_gcs(model, bucket)
    
    # Evaluate model
    test_loss, test_accuracy = performance_utils.evaluate_model(model, X_test, y_test)
    performance_utils.plot_roc_curve(model, X_test, y_test)

if __name__ == "__main__":
    main()