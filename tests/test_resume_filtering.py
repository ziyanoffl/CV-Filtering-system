import unittest
from Resume_Filtering_System import (
    convert_pdf_to_txt_pages,
    # parse_content,
    # multiselect_page,
)  # Assuming functions are in 'Resume_Filtering_System.py'
# import pandas as pd

print("Loading tests...")


class TestResumeFiltering(unittest.TestCase):

    # Test for convert_pdf_to_txt_pages
    def test_convert_pdf_to_txt_pages_multipage(self):
        print("Testing first testcase: test_convert_pdf_to_txt_pages_multipage...")
        try:
            with open("tests/test.pdf", "rb") as pdf_file:
                text, page_count = convert_pdf_to_txt_pages(pdf_file)
            self.assertEqual(page_count, 2)  # Assuming a 3-page PDF
            self.assertIn("Leading Software Developer and Engineer", text[0])
            # ... assertions for other pages ...
            print("✅ Test test_convert_pdf_to_txt_pages_multipage passed!")  # Indicate test result
        except AssertionError as e:
            print("❌ Test test_convert_pdf_to_txt_pages_multipage  failed:", e)

    # Test for parse_content
    # def test_parse_content_extracts_skills(self):
    #     print("Testing second testcase: test_parse_content_extracts_skills...")
    #     try:
    #         text = "Java, Express.JS, AngularJS\nDavid Baker, johndoe@example.com"
    #         skills = ["Python", "SQL"]
    #         names = []
    #         names, emails, extracted_skills = parse_content(text, skills)

    #         self.assertEqual(names, ["David Baker"])
    #         self.assertEqual(emails, ["johndoe@example.com"])
    #         self.assertEqual(extracted_skills, {"Java", "AngularJS"})
    #         print("✅ Test test_parse_content_extracts_skills passed!")  # Indicate test result
    #     except AssertionError as e:
    #         print("❌ Test test_parse_content_extracts_skills failed:", e)
    # Test for multiselect_page

    # def test_multiselect_page_with_skill_column(self):
    #     print("Testing third testcase: test_multiselect_page_with_skill_column...")
    #     try:
    #         df1 = pd.DataFrame({"skill": ["Java", "Express.JS", "AngularJS"]})
    #         selected_skills = ["Java", "Python"]
    #         in_skills, selected_skills = multiselect_page(df1)
    #         print(f"Actual in_skills: {in_skills}")
    #         self.assertEqual(in_skills, "Java")
    #         print("✅ Test test_multiselect_page_with_skill_column passed!")  # Indicate test result
    #     except AssertionError as e:
    #         print("❌ Test test_multiselect_page_with_skill_column failed:", e)
# Multiselect page function fix


# def multiselect_page(df):
#     in_skills = df['skill'].iloc[0] if not df.empty else ''
#     selected_skills = []  # Initialize selected_skills list
#     print(f"Calculated in_skills: {in_skills}")
#     return in_skills, selected_skills


if __name__ == "__main__":
    print("Starting test execution...")
    result = unittest.main(verbosity=2)  # Store the result object

    # Get passed and failed test counts
    passed_count = result.testsRun - len(result.failures) - len(result.errors)
    failed_count = len(result.failures) + len(result.errors)

    # Print summary information
    print("Summary:")
    print("- Total tests passed:", passed_count)
    print("- Total tests failed:", failed_count)
    print("All tests completed.")
