import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

model = load_model("model/detector_model.h5")

def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

def classify_image(image):
    processed = preprocess_image(image)
    prediction = model.predict(processed)[0][0]

    label = "AI-Generated" if prediction > 0.5 else "Real"
    confidence = prediction * 100 if prediction > 0.5 else (1 - prediction) * 100

    return label, confidence
