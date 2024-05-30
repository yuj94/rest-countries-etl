import pytest
import requests
from fetch_data import fetch_countries

# Fixture to mock the API response
@pytest.fixture
def mock_response(monkeypatch):
    class MockResponse:
        @staticmethod
        def json():
            return [
                {
                    "name": {"official": "Test Country"}, 
                    "cioc": "TC", 
                    "currencies": {"USD": {}}
                }
            ]
        
        @staticmethod
        def raise_for_status():
            pass

    monkeypatch.setattr(requests, "get", lambda url: MockResponse())

# Test for successful data fetch
def test_fetch_countries(mock_response):
    url = "https://restcountries.com/v3.1/all"
    countries = fetch_countries(url)
    assert isinstance(countries, list)
    assert len(countries) > 0

# Negative test: API returns an error
def test_fetch_countries_api_error(monkeypatch):
    class MockResponse:
        @staticmethod
        def raise_for_status():
            raise requests.exceptions.HTTPError("API error")

    monkeypatch.setattr(requests, "get", lambda url: MockResponse())

    url = "https://restcountries.com/v3.1/all"
    with pytest.raises(requests.exceptions.HTTPError):
        fetch_countries(url)
