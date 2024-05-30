import pytest
from transform_data import transform_countries

# Fixture for sample country data
@pytest.fixture
def sample_countries():
    return [
        {
            "cca2": "TC",
            "name": {"official": "Test Country"}, 
            "cioc": "TC", 
            "currencies": {"USD": {}}, 
            "region": "Test Region"
        }
    ]

# Test for successful data transformation
def test_transform_countries(sample_countries):
    transformed = transform_countries(sample_countries)
    assert not transformed.empty
    assert "id" in transformed.columns
    assert "country_name" in transformed.columns
    assert "country_code" in transformed.columns
    assert "currencies" in transformed.columns
    assert "region" in transformed.columns
    assert "updated_date" in transformed.columns
    assert "updated_by" in transformed.columns

# Edge case: Empty country data
def test_transform_countries_empty():
    transformed = transform_countries([])
    assert transformed.empty

# Edge case: Missing fields in country data
def test_transform_countries_missing_fields():
    incomplete_countries = [{"name": {"official": "Test Country"}}]
    transformed = transform_countries(incomplete_countries)
    assert transformed.at[0, 'id'] == ''
    assert transformed.at[0, 'country_code'] == ''
    assert transformed.at[0, 'currencies'] == ''
    assert transformed.at[0, 'region'] == ''
