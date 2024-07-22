# this file as all the code together other fies are not the part of this file 

import streamlit as st
from PIL import Image
import pytesseract
import google.generativeai as genai
import json
import re

# Configure generative AI with the API key
genai.configure(api_key="Please add key here")


# Function to process text using generative AI
def process_text_to_json(text, keys):
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Extract the following data based on these keys and return in JSON format. For keys not present in the text, place 'None' in the response: {', '.join(keys)}.\n\nExtracted Data:\n{text}"

        # Generate content using the model
        response = model.generate_content(prompt)

        # Extract JSON string from response
        response_text = response.candidates[0].content.parts[0].text

        # Debugging: Print the raw response text
        st.write("Raw response text:")
        st.code(response_text)

        # Use regular expressions to remove unwanted characters
        json_str = re.sub(r'^\s*```+', '', response_text)  # Remove leading ``` or '''
        json_str = re.sub(r'```+\s*$', '', json_str)  # Remove trailing ``` or '''

        # Debugging: Print cleaned JSON string
        st.write("Cleaned JSON string:")
        st.code(json_str)

        # Parse the JSON string
        try:
            json_data = json.loads(json_str)
            return json_data
        except json.JSONDecodeError as e:
            st.error(f"JSON decoding error: {e}")
            st.error(f"Response text: {json_str}")
            return None
    except Exception as e:
        st.error(f"An error occurred while processing text with generative AI: {e}")
        return None


# Function to extract text from the image
def extract_text_from_image(image):
    return pytesseract.image_to_string(image)


# Title of the application
st.title('Image to JSON Key-Value Pairs')

# Image upload
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image:
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
            extracted_data = process_text_to_json(extracted_text, keys)
            if extracted_data:
                st.write("Extracted Key-Value Pairs:")
                st.json(extracted_data)
            else:
                st.error("Failed to extract key-value pairs.")
