from PIL import Image
import pytesseract

def extract_text_from_image(image: Image.Image) -> str:
    """
    Extract text from an image using pytesseract.
    """
    return pytesseract.image_to_string(image)
