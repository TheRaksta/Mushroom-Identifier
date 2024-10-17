from flask import Flask, request, jsonify
from utils.cloud_utils import connect_to_gcs, get_bucket
from utils.model_utils import load_latest_model
from inference.predictor import MushroomPredictor
from config import config

app = Flask(__name__)

# Load the model at startup
client = connect_to_gcs()
bucket = get_bucket(client)
model = load_latest_model(bucket)
predictor = MushroomPredictor(model)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image = request.files['image']
    result = predictor.predict(image)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)