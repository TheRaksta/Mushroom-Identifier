from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
from model_deployment.utils.image_utils import preprocess_image
import io

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def upload_image(file: UploadFile = File(...)):
    # Check if the file is an image
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG or PNG images are supported.")

    # Read the image content
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # turn image to numpy array
    numpy_array = preprocess_image(image)

    # fetch model


    # run prediction

    # pass reponse
