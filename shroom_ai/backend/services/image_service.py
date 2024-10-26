# backend/services/image_service.py
import numpy as np
from PIL import Image
import io
from fastapi import UploadFile

class ImageService:
    def __init__(self, target_size=(224, 224)):
        self.target_size = target_size

    async def process_image(self, file: UploadFile) -> np.ndarray:
        """
        Process uploaded image file into the format required by the model.
        """
        # Read image file
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))

        # Convert to RGB if needed
        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Resize image
        image = image.resize(self.target_size, Image.Resampling.LANCZOS)

        # Convert to numpy array and normalize
        image_array = np.array(image) / 255.0

        # Add batch dimension
        return np.expand_dims(image_array, axis=0)