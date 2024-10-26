# backend/services/model_service.py
import tensorflow as tf
import numpy as np

class ModelService:
    def __init__(self, model_path: str):
        """
        Initialize the model service with the path to the saved model.
        """
        self.model = tf.keras.models.load_model(model_path)

    def predict(self, image_array: np.ndarray) -> dict:
        """
        Make a prediction on the processed image.
        Returns dictionary with prediction and confidence.
        """
        # Make prediction
        prediction = self.model.predict(image_array)[0][0]
        
        # Convert to binary prediction with confidence
        is_edible = prediction >= 0.5
        confidence = float(prediction if is_edible else 1 - prediction)

        return {
            "is_edible": bool(is_edible),
            "confidence": confidence
        }
