# tests/test_resume_filtering.py
import unittest
from Resume_Filtering_System import convert_pdf_to_txt_pages

class TestResumeFiltering(unittest.TestCase):
    def test_convert_pdf_to_txt_pages(self):
        # Replace 'path/to/test.pdf' with the path to a sample PDF for testing
        pdf_path = '/Viththiyatharan_Resume.pdf'
        result, num_pages = convert_pdf_to_txt_pages(pdf_path)

        # Assertion 1: Ensure the result is not None
        self.assertIsNotNone(result)

        # Assertion 2: Ensure the result is a list
        self.assertIsInstance(result, list)

        # Assertion 3: Ensure the number of pages is greater than 0
        self.assertGreater(num_pages, 0)

if __name__ == '__main__':
    unittest.main()
