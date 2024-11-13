import re
import io
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np

def remove_newlines(text):
    # Remove newlines
    new_text = re.sub(r'\s+', '', text)
    return new_text

def convert_bytes_to_pil_image(image_bytes):
    """Convert raw image bytes to a PIL Image."""
    image_stream = io.BytesIO(image_bytes)  # Convert the image bytes to an in-memory byte stream
    pil_image = Image.open(image_stream)    # Open the byte stream with PIL
    return pil_image

def preprocess_image(pil_image):
    """Preprocess the image to improve OCR accuracy."""
    # Convert PIL image to an OpenCV image (numpy array)
    image = np.array(pil_image)
    
    # Step 1: Grayscale Conversion - Convert the image to grayscale
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image

    # Step 2: Adaptive Thresholding - Binarize the image adaptively
    adaptive_binary = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Convert back to a PIL image
    preprocessed_pil_image = Image.fromarray(adaptive_binary)

    # Debug: Visualize the preprocessed image for OCR
    plt.imshow(preprocessed_pil_image, cmap='gray')
    plt.title('Preprocessed Image for OCR')
    plt.axis('off')
    plt.show()

    return preprocessed_pil_image

def find_pattern_in_text(text, pattern):
    """Find all occurrences of a pattern in the text."""
    matches = re.findall(pattern, text)
    return matches