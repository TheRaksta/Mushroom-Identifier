from utils.image_utils import preprocess_image

class MushroomPredictor:
    def __init__(self, model):
        self.model = model

    def predict(self, image):
        processed_image = preprocess_image(image)
        prediction = self.model.predict(processed_image)[0][0]
        is_edible = prediction > 0.5
        confidence = prediction if is_edible else 1 - prediction
        return {
            "is_edible": bool(is_edible),
            "confidence": float(confidence),
            "raw_score": float(prediction)
        }