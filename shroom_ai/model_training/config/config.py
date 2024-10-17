# config/config.py

# Google Cloud Storage settings
GCS_PROJECT_ID = ""
GCS_BUCKET_NAME = ""
GCS_IMAGE_PREFIX = "images/"
GCS_MODEL_PREFIX = "models/"

# Data processing settings
IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32

# Model settings
LEARNING_RATE = 0.001
DENSE_UNITS = 224
EPOCHS = 50

# Training settings
VALIDATION_SPLIT = 0.2
TEST_SPLIT = 0.2
RANDOM_SEED = 42