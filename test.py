import tensorflow as tf
import numpy as np
from PIL import Image

# load model (make sure file is in backend)
model = tf.keras.models.load_model("leaf_model.keras")

# your classes (same order as dataset folders)
classes = [
    "Pepper__bell___Bacterial_spot",
    "Potato___Late_blight",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___Bacterial_spot"
]

# load test image
img = Image.open("test.png").resize((128,128))
img = np.array(img)/255.0
img = np.expand_dims(img, axis=0)

# predict
pred = model.predict(img)
idx = np.argmax(pred)

print("Disease:", classes[idx])
print("Confidence:", round(float(pred[0][idx])*100, 2), "%")