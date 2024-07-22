import streamlit as st
from PIL import Image
from image_processing import extract_text_from_image
from api_integration import process_text_to_json
from logging_handler import setup_logging, log_error

# Setup logging
logger = setup_logging()

# Title of the application
st.title('Image to JSON Key-Value Pairs')

# Image upload
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image:
    try:
        # Display the uploaded image
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Extract text from the image
        extracted_text = extract_text_from_image(image)
        st.write("Extracted Text:")
        st.write(extracted_text)

        # Input keys
        keys_input = st.text_input("Enter the keys to extract, separated by commas:")

        if keys_input:
            keys = [key.strip() for key in keys_input.split(',')]

            # Button to process the text and extract key-value pairs
            if st.button("Extract Key-Value Pairs"):
                # Process the text using generative AI
                extracted_data = process_text_to_json(extracted_text, keys)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        log_error(logger, e)
