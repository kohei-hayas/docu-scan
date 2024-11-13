import unittest
from src.text_processing import extract_text_from_pdf, extract_text_from_pptx, extract_text_from_docx
class TestTextProcessing(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        """Test text extraction from PDF files."""
        pdf_path = "data/example.pdf"
        text = extract_text_from_pdf(pdf_path)
        # Log the first and last 100 characters of the extracted text
        print("PDF Text:", text)
        # Check if some text was extracted (assuming the sample contains text)
        self.assertIsNotNone(text)
        self.assertGreater(len(text.strip()), 0, "The extracted text from PDF should not be empty.")
    
    def test_extract_text_from_pptx(self):
        """Test text extraction from PPTX files."""
        pptx_path = "data/example.pptx"
        text = extract_text_from_pptx(pptx_path)
        # Log the first and last 100 characters of the extracted text
        print("PPTX Text:", text)
        # Check if some text was extracted (assuming the sample contains text)
        self.assertIsNotNone(text)
        self.assertGreater(len(text.strip()), 0, "The extracted text from PPTX should not be empty.")
    
    def test_extract_text_from_docx(self):
        """Test text extraction from DOCX files."""
        docx_path = "data/example.docx"
        text = extract_text_from_docx(docx_path)
        # Log the first and last 100 characters of the extracted text
        print("DOCX Text:", text)
        # Check if some text was extracted (assuming the sample contains text)
        self.assertIsNotNone(text)
        self.assertGreater(len(text.strip()), 0, "The extracted text from DOCX should not be empty.")

if __name__ == "__main__":
    unittest.main()