from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
import numpy as np
from PIL import Image
import os

app = Flask(__name__)
CORS(app)

# load model
model = tf.keras.models.load_model("leaf_model.keras")

# disease info
disease_info = {
    "Pepper__bell___Bacterial_spot": {
        "name": "Pepper Bacterial Spot",
        "cause": "Bacterial infection due to moisture",
        "cure": "Use copper spray",
        "prevention": "Avoid wet leaves"
    },
    "Potato___Late_blight": {
        "name": "Potato Late Blight",
        "cause": "Fungus in cool wet weather",
        "cure": "Apply fungicide",
        "prevention": "Ensure drainage"
    },
    "Tomato___Tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "cause": "Virus spread by tools",
        "cure": "Remove infected plant",
        "prevention": "Use clean tools"
    },
    "Tomato___Bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "cause": "Bacteria in humidity",
        "cure": "Use bactericide",
        "prevention": "Avoid overhead watering"
    }
}

classes = list(disease_info.keys())

@app.route("/")
def home():
    return "LeafCare AI running"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        file = request.files["file"]

        # Image processing
        img = Image.open(file).convert("RGB")
        img = img.resize((128, 128))

        img = np.array(img) / 255.0
        img = np.expand_dims(img, axis=0)

        pred = model.predict(img)
        idx = int(np.argmax(pred))

        key = classes[idx]
        info = disease_info[key]

        return jsonify({
            "disease": info["name"],
            "confidence": float(round(pred[0][idx] * 100, 2)),
            "cause": info["cause"],
            "cure": info["cure"],
            "prevention": info["prevention"]
        })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)})

# ✅ Deployment-safe run
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)