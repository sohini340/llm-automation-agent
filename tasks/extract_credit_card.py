import pytesseract
from PIL import Image
import re
import os

def process():
    """Extract a credit card number from an image using OCR."""
    input_file = "/data/credit_card.png"
    output_file = "/data/credit-card.txt"

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"{input_file} does not exist")

    # Load the image
    image = Image.open(input_file)

    # Extract text using OCR
    extracted_text = pytesseract.image_to_string(image)

    # Find the credit card number (assuming a standard 16-digit format)
    match = re.search(r"\b(\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4})\b", extracted_text)

    if match:
        # Remove spaces and dashes
        card_number = match.group(1).replace(" ", "").replace("-", "")

        # Save to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(card_number)

        return f"Extracted card number saved to {output_file}"
    
    return "No valid credit card number found."

