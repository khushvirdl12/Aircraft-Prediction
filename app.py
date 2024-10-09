import streamlit as st
import pickle
from PIL import Image
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Function to process the image and make predictions
def identify_aircraft(image):
    # Preprocess the image to the required format
    img_array = np.array(image)
    img_array = img_array.reshape(1, -1)  # Adjust this based on your model's input requirements
    # Predict using the loaded model
    prediction = model.predict(img_array)
    return prediction

# Streamlit interface
st.title('Aircraft Identifier')
st.write('Upload an image of an aircraft to identify it.')

uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Identifying...")

    # Identify the aircraft
    prediction = identify_aircraft(image)

    st.write(f"Prediction: {prediction}")
