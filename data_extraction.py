import pytesseract
from PIL import Image

def extract_data_from_image(image: Image.Image):
    # Convert image to text using pytesseract
    text = pytesseract.image_to_string(image)

    return text
