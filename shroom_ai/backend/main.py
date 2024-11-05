# backend/main.py (modified section)
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.image_service import ImageService
from services.model_service import ModelService
from config.settings import Settings

app = FastAPI(title="Mushroom Classification API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
settings = Settings()
image_service = ImageService()
model_service = ModelService(
    edible_model_path=settings.EDIBLE_MODEL_PATH,
    species_model_path=settings.SPECIES_MODEL_PATH
)

@app.post("/classify")
async def classify_mushroom(file: UploadFile = File(...)):
    """
    Endpoint to classify whether a mushroom is edible and identify its species if edible.
    Returns predictions and confidence scores.
    """
    try:
        image_array = await image_service.process_image(file)
        prediction = model_service.predict(image_array)
        
        response = {
            "edible": prediction["is_edible"],
            "confidence": prediction["edible_confidence"]
        }
        
        if prediction["is_edible"]:
            response.update({
                "species_predictions": prediction["species_predictions"],
                "species_total_confidence": prediction["species_total_confidence"]
            })
            
        return response
    except Exception as e:
        return {"error": str(e)}, 400