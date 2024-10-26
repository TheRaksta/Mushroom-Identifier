# backend/main.py
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.image_service import ImageService
from services.model_service import ModelService
from config.settings import Settings

app = FastAPI(title="Mushroom Classification API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your Streamlit app URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
settings = Settings()
image_service = ImageService()
model_service = ModelService(settings.MODEL_PATH)

@app.post("/classify")
async def classify_mushroom(file: UploadFile = File(...)):
    """
    Endpoint to classify whether a mushroom is edible or not.
    Returns a prediction and confidence score.
    """
    # Process the uploaded image
    try:
        image_array = await image_service.process_image(file)
        prediction = model_service.predict(image_array)
        
        return {
            "edible": bool(prediction["is_edible"]),
            "confidence": float(prediction["confidence"])
        }
    except Exception as e:
        return {"error": str(e)}, 400