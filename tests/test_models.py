import pytest
from models import Country

# Test for successful Country model creation and conversion to dictionary
def test_country_model():
    country = Country(
        id="TC",
        country_name="Test Country",
        country_code="TC",
        currencies="USD",
        region="Test Region",
        updated_date="2024-05-29",
        updated_by="system"
    )
    country_dict = country.to_dict()
    assert country_dict["id"] == "TC"
    assert country_dict["country_name"] == "Test Country"
    assert country_dict["country_code"] == "TC"
    assert country_dict["currencies"] == "USD"
    assert country_dict["region"] == "Test Region"
    assert country_dict["updated_date"] == "2024-05-29"
    assert country_dict["updated_by"] == "system"

# Edge case: Empty fields
def test_country_model_empty_fields():
    country = Country(
        id="",
        country_name="",
        country_code="",
        currencies="",
        region="",
        updated_date="",
        updated_by=""
    )
    country_dict = country.to_dict()
    assert country_dict["id"] == ""
    assert country_dict["country_name"] == ""
    assert country_dict["country_code"] == ""
    assert country_dict["currencies"] == ""
    assert country_dict["region"] == ""
    assert country_dict["updated_date"] == ""
    assert country_dict["updated_by"] == ""
