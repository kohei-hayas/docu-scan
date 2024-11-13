import unittest
from src.utils import remove_newlines
from src.image_processing import extract_image_text_pdf, extract_image_text_pptx, extract_image_text_docx

class TestImageProcessing(unittest.TestCase):
    """Test text extraction from PDF, PPTX, and DOCX files."""
    def test_extract_image_text_pdf(self):
        pdf_path = "data/example.pdf"
        text = extract_image_text_pdf(pdf_path)
        # Print all extracted text from the PDF
        print("PDF Text:", remove_newlines(text))
        # Check if some text was extracted (assuming the sample contains text)
        self.assertIsNotNone(text)
        self.assertGreater(len(text.strip()), 0, "The extracted text from PDF should not be empty.")
    
    def test_extract_image_text_pptx(self):
        pptx_path = "data/example.pptx"
        text = extract_image_text_pptx(pptx_path)
        # Print all extracted text from the PPTX
        print("PPTX Text:", remove_newlines(text))
        # Check if some text was extracted (assuming the sample contains text)
        self.assertIsNotNone(text)
        self.assertGreater(len(text.strip()), 0, "The extracted text from PPTX should not be empty.")

    def test_extract_image_text_docx(self):
        docx_path = "data/example.docx"
        text = extract_image_text_docx(docx_path)
        # Print all extracted text from the DOCX
        print("DOCX Text:", remove_newlines(text))
        # Check if some text was extracted (assuming the sample contains text)
        self.assertIsNotNone(text)
        self.assertGreater(len(text.strip()), 0, "The extracted text from DOCX should not be empty.")

if __name__ == "__main__":
    unittest.main()
