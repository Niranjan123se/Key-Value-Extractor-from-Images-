import google.generativeai as genai
import json
import streamlit as st
import re

# Configure generative AI with the API key
genai.configure(api_key="Please add your key")

def process_text_to_json(text: str, keys: list) -> dict:
    """
    Process text using generative AI to extract key-value pairs based on the provided keys.
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        prompt = f"Extract the following data based on these keys and return in JSON format. For keys not present in the text, place 'None' in the response: {', '.join(keys)}.\n\nExtracted Data:\n{text}"

        # Generate content using the model
        response = model.generate_content(prompt)

        # Extract JSON string from response
        response_text = response.candidates[0].content.parts[0].text


        # Use regular expressions to remove unwanted characters
        json_str = re.sub(r'^\s*```+', '', response_text)  # Remove leading ``` or '''
        json_str = re.sub(r'```+\s*$', '', json_str)  # Remove trailing ``` or '''

        # Debugging: Print cleaned JSON string
        st.write("Cleaned JSON string:")
        st.code(json_str)

    #     # Parse the JSON string
    #     try:
    #         json_data = json.loads(json_str)
    #         return json_data
    #     except json.JSONDecodeError as e:
    #         st.error(f"JSON decoding error: {e}")
    #         st.error(f"Response text: {json_str}")
    #         return None
    except Exception as e:
        st.error(f"An error occurred while processing text with generative AI: {e}")
        return None
