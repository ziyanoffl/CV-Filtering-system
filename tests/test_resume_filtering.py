import unittest
from Resume_Filtering_System import convert_pdf_to_txt_pages

class TestResumeFiltering(unittest.TestCase):
    def test_convert_pdf_to_txt_pages(self):
 
        pdf_path = '/Viththiyatharan_Resume.pdf'
        result, num_pages = convert_pdf_to_txt_pages(pdf_path)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertGreater(num_pages, 0)

if __name__ == '__main__':
    unittest.main(argv=['-qq', '--with-junitxml=unittest_results.xml'])
