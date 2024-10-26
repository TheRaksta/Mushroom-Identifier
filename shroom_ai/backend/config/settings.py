# backend/config/settings.py
from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    # Model settings
    MODEL_PATH: str = "../../../models/models_mushroom_classification_model_20241026_094856.h5"
    
    # API settings
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    class Config:
        env_file = ".env"