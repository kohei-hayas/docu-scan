# Document Pattern Detection Program

This program detects specific string patterns within various document types, including PDFs, PowerPoint presentations, and Word documents. The documents may also contain images that require Optical Character Recognition (OCR) for extracting text. The following README outlines how to extract text and images and use regex to search for patterns.

## Prerequisites
To develop and run this program, you will need the following libraries and tools installed:

### Python Libraries
- `pytesseract`: OCR processing
- `pdf2image`: Convert PDF pages to images
- `pymupdf` (PyMuPDF): Extract text from PDF
- `python-pptx`: Extract text and images from PowerPoint files
- `python-docx`: Extract text and images from Word documents
- `Pillow`: Image manipulation

Install these libraries via pip:
```bash
pip install pytesseract pdf2image pymupdf python-pptx python-docx Pillow
```

### Tesseract-OCR
Make sure **Tesseract-OCR** is installed and available in your system's PATH:
- On Linux: `sudo apt-get install tesseract-ocr`
- On macOS (with Homebrew): `brew install tesseract`
- On Windows: [Download and install Tesseract](https://github.com/UB-Mannheim/tesseract/wiki)

## Development Environment
- **Mac**: This program is developed on macOS.
- **Windows**: The program will also be used on a Windows system. Ensure that all the necessary dependencies are installed and paths are configured correctly for Windows compatibility.

## File Types Supported
- **PDFs**: Extract both text and images. OCR is applied to extract text from images.
- **PowerPoint (.pptx)**: Extract text and embedded images from slides.
- **Word (.docx)**: Extract text and embedded images from paragraphs.

## Workflow Summary
### 1. Extract Text and Images
- **PDF Handling**:
  - Use **PyMuPDF** to extract text.
  - Use **pdf2image** to convert PDF pages to images, and **Pytesseract** for OCR.

- **PowerPoint Handling**:
  - Use **python-pptx** to extract text and images from slides.
  - Convert image byte data to a Pillow image and apply **Pytesseract** for OCR.

- **Word Document Handling**:
  - Use **python-docx** to extract text and images.
  - Convert image bytes to a Pillow image and apply **Pytesseract** for OCR.

### 2. Process Images in Memory
- Convert extracted image bytes to a Pillow image using **io.BytesIO**.
- Use **Pytesseract** to perform OCR on these in-memory images.

### 3. Pattern Matching
- After text extraction, use **regex** to search for specific patterns.
- Example function for pattern matching:
  ```python
  import re

  def find_pattern_in_text(text, pattern):
      return re.findall(pattern, text)
  ```

### 4. Combine the Workflow
Create a unified function or script that handles each document type, extracts all content, and applies regex to detect the desired pattern.


## Project File Structure
To keep the project organized and maintainable, the following file structure is recommended:

```
document_pattern_detection/
├── venv/                  # Virtual environment folder (usually not included in version control)
├── data/                  # Folder for storing sample documents (PDFs, PPTX, DOCX) for testing
│   ├── example.pdf
│   ├── example.pptx
│   └── example.docx
├── output/                # Folder to store any output files, such as extracted text or logs
│   ├── extracted_text.txt
│   └── logs.txt
├── src/                   # Source code folder
│   ├── main.py            # Main entry point for the application
│   ├── text_processing.py # Functions for extracting text from PDFs, PPTX, DOCX
│   ├── image_processing.py # Functions for processing images (e.g., OCR using Pytesseract)
│   ├── utils.py           # Utility functions (e.g., regex searching, file I/O helpers)
│   └── config.py          # Configuration settings (e.g., paths, constants)
├── tests/                 # Folder for unit and integration tests
│   ├── test_text_processing.py
│   ├── test_image_processing.py
│   └── test_utils.py
├── requirements.txt       # Dependencies
└── README.md              # Project documentation (already created)
```

### Breakdown of Each Component
1. **`venv/`**: The virtual environment folder, which is typically excluded from version control (`.gitignore`). This keeps all dependencies contained locally.

2. **`data/`**: This is where you store sample documents used for testing. It can be useful for running local tests or development without using real user documents.

3. **`output/`**: This directory stores any output, like extracted text or log files. This helps keep your project directory organized.

4. **`src/`** (Source Code Folder):
   - **`main.py`**: Acts as the entry point for running the entire workflow. Handles high-level logic, such as reading file paths from the user, calling different functions for text or image processing, and printing or saving the results.
   - **`text_processing.py`**: Contains all functions for extracting text from PDFs, PPTX, and DOCX. Keeps code modular by separating text processing from image processing.
   - **`image_processing.py`**: Contains the code for extracting images from different document formats and applying OCR using Pytesseract. Since the image processing workflow is the same after image extraction, this file keeps those functions consistent and reusable.
   - **`utils.py`**: Contains utility functions that are shared across different files. This could include functions for searching text patterns using regex, file handling, and converting file paths for compatibility across operating systems.
   - **`config.py`**: Stores configuration settings such as directory paths, constant variables, Tesseract path settings, etc. Centralizes configuration to easily adjust paths or settings without altering the main code.

5. **`tests/`**: Contains unit and integration tests to verify the correctness of text and image extraction and pattern matching. The folder includes separate test files for each core functionality (`text_processing.py`, `image_processing.py`, and `utils.py`). This ensures that each function behaves correctly in isolation.

6. **`requirements.txt`**: Lists all required dependencies. This makes it easy to set up the environment on different systems.

7. **`README.md`**: Already created to provide documentation and setup instructions.

## Next Steps
1. **Write and Test Individual Functions**: Implement the extraction functions for each document type and test them individually.
2. **Integrate Functions**: Combine text and image extraction into a single workflow, ensuring comprehensive text coverage.
3. **Refinement**: Fine-tune OCR settings to improve accuracy and optimize regex for pattern matching.

## Note for Windows Compatibility
When transitioning to Windows, ensure:
- **Tesseract-OCR** is installed and added to the system PATH.
- Paths are correctly formatted for Windows (use double backslashes `\` or raw strings `r"path"`).

Feel free to reach out if you encounter any issues or need further assistance while setting up or running the program!

