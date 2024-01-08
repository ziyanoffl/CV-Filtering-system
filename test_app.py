import pytest
from io import StringIO
from click.testing import CliRunner
from Resume_Filtering_System import convert_pdf_to_txt_pages, parse_content

@pytest.fixture
def sample_pdf_path():
    return r"/Users/sharma/Desktop/untitled folder/CV-Filtering-system/tests/test.pdf"  # Replace with an actual PDF path for testing

def test_convert_pdf_to_txt_pages(sample_pdf_path):
    texts, nbPages = convert_pdf_to_txt_pages(sample_pdf_path)
    assert isinstance(texts, list)
    assert isinstance(nbPages, int)
    assert len(texts) == nbPages

def test_parse_content():
    text = "Sample resume text with skills Python and SQL"
    in_skills = "Python|SQL"

    # Initialize names, emails, and skills
    names = []
    emails = []
    skills = []

    # Update parse_content function if needed to accept additional parameters
    parse_content(text, in_skills)

    assert len(emails) == 0  # Replace with the expected number of emails
    assert len(skills) == 2  # Replace with the expected number of skills
    # Add more assertions based on the expected behavior

# Add more tests as needed

if __name__ == "__main__":
    pytest.main(["-v", "test_app.py"])
