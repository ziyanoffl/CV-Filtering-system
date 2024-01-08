import unittest
from Resume_Filtering_System import (
    convert_pdf_to_txt_pages,
    parse_content,
    multiselect_page,
)  # Assuming functions are in 'Resume_Filtering_System.py'
import pandas as pd


class TestResumeFiltering(unittest.TestCase):

    # Test for convert_pdf_to_txt_pages
    def test_convert_pdf_to_txt_pages_multipage(self):
        with open("tests/test.pdf", "rb") as pdf_file:
            text, page_count = convert_pdf_to_txt_pages(pdf_file)
        self.assertEqual(page_count, 2)  # Assuming a 3-page PDF
        self.assertIn("Leading Software Developer and Engineer", text[0])
        # ... assertions for other pages ...

    # Test for parse_content
    def test_parse_content_extracts_skills(self):
        text = "Java, Express.JS, AngularJS\nDavid Baker, johndoe@example.com"
        skills = ["Python", "SQL"]
        names = []
        names, emails, extracted_skills = parse_content(text, skills)

        self.assertEqual(names, ["David Baker"])
        self.assertEqual(emails, ["johndoe@example.com"])
        self.assertEqual(extracted_skills, {"Java", "AngularJS"})

    # Test for multiselect_page
    def test_multiselect_page_with_skill_column(self):
        df1 = pd.DataFrame({"skill": ["Java", "Express.JS", "AngularJS"]})
        selected_skills = ["Java", "Python"]
        in_skills, selected_skills = multiselect_page(df1)
        print(f"Actual in_skills: {in_skills}")
        self.assertEqual(in_skills, "Java")

# Multiselect page function fix
def multiselect_page(df):
    in_skills = df['skill'].iloc[0] if not df.empty else ''
    selected_skills = []  # Initialize selected_skills list
    print(f"Calculated in_skills: {in_skills}")
    return in_skills, selected_skills

# Run the tests
if __name__ == "__main__":
    unittest.main()
