# backend/config/settings.py
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Model settings
    EDIBLE_MODEL_PATH: str = "../../../models/models_mushroom_classification_model_20241026_094856.h5"
    SPECIES_MODEL_PATH: str = "../../../models/models_mushroom_species_model_20241102_204535.h5"
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    class Config:
        env_file = ".env"