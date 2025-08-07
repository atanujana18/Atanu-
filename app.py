import streamlit as st
from PIL import Image
import numpy as np
from utils.predict import classify_image

st.set_page_config(page_title="AI vs Real Image Detector", layout="centered")

st.title("🧠 Real vs AI-Generated Image Detector")
st.write("Upload an image and let the AI decide if it's real or AI-generated.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing..."):
        label, confidence = classify_image(image)

    st.success(f"**Prediction:** {label}")
    st.info(f"**Confidence:** {confidence:.2f}%")
