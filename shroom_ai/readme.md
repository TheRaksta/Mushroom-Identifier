# Shroom AI

Shroom AI is a machine learning project for classifying mushrooms as edible or poisonous using image recognition. The project is divided into two main components: model training and model deployment.

To start the project, run ./run_dev

## Project Structure

```
shroom_ai/
├── model_training/
│   ├── config/
│   ├── data/
│   ├── models/
│   ├── utils/
│   └── main.py
├── model_deployment/
│   ├── config/
│   ├── utils/
│   ├── inference/
│   └── app.py
├── requirements.txt
└── README.md
```

## Model Training

The `model_training` folder contains all the necessary code to train the mushroom classification model using images stored in Google Cloud Storage.

### Setup

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Set up Google Cloud credentials:
   - Create a service account key in the Google Cloud Console
   - Download the JSON key file
   - Set the environment variable:
     ```
     export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-key.json"
     ```

3. Update the configuration:
   - Edit `model_training/config/config.py` with your Google Cloud project details and desired model parameters

### Training the Model

To train the model:

1. Navigate to the `model_training` folder:
   ```
   cd shroom_ai/model_training
   ```

2. Run the training script:
   ```
   python main.py
   ```

This script will:
- Connect to Google Cloud Storage
- Load and preprocess the mushroom images
- Build and train the classification model
- Save the trained model back to Google Cloud Storage

## Model Deployment

The `model_deployment` folder contains the code for deploying the trained model as a Flask API for real-time inference.

### Setup

1. Ensure you have installed all required packages from `requirements.txt`

2. Set up Google Cloud credentials (if not already done in the training step)

3. Update the configuration:
   - Edit `model_deployment/config/config.py` with your Google Cloud project details and Flask app settings

### Running the Inference API

To start the Flask API for mushroom classification:

1. Navigate to the `model_deployment` folder:
   ```
   cd shroom_ai/model_deployment
   ```

2. Run the Flask app:
   ```
   python app.py
   ```

This will start a Flask server that:
- Loads the most recent model from Google Cloud Storage
- Exposes a `/predict` endpoint for mushroom classification

### Using the API

To classify a mushroom image:

1. Send a POST request to `http://localhost:5000/predict` (adjust the host and port if necessary)
2. Include the image file in the request body with the key 'image'

Example using curl:
```
curl -X POST -F "image=@/path/to/mushroom_image.jpg" http://localhost:5000/predict
```

The API will return a JSON response with the classification result:
```json
{
  "is_edible": true,
  "confidence": 0.95,
  "raw_score": 0.95
}
```

## Maintenance and Updates

### Updating the Model

To update the model:
1. Add new training data to the appropriate Google Cloud Storage bucket
2. Run the training script in the `model_training` folder
3. The new model will be automatically saved to Google Cloud Storage

The deployment API will automatically use the latest model for predictions, so no further action is needed.

