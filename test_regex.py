import pytest #import test library
from regex import validate_email, extract_domain # imports 2 defs from regex.py

def test_validate_email():
    # Test valid emails
    assert validate_email("valid@example.com") 
    assert validate_email("user.name+tag@example.co.uk") 

    # Test invalid emails
    assert validate_email("invalid-email") is None
    assert validate_email("@missingusername.com") is None


def test_extract_domain():
    # Test valid email domains
    assert extract_domain("valid@example.com") == "example.com"
    assert extract_domain("user.name+tag@example.co.uk") == "example.co.uk"

   

def test_extract_domain_no_at_symbol():
    # Tests where there is no @ symbol
    assert extract_domain("username.domain.com") is None