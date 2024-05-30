import pytest
import pandas as pd
import os
from save_data import save_to_csv

# Fixture for sample DataFrame
@pytest.fixture
def sample_dataframe():
    data = {
        "id": ["TC"],
        "country_name": ["Test Country"],
        "country_code": ["TC"],
        "currencies": ["USD"],
        "region": ["Test Region"],
        "updated_date": ["2024-05-29"],
        "updated_by": ["system"]
    }
    return pd.DataFrame(data)

# Test for successful CSV save
def test_save_to_csv(sample_dataframe, tmp_path):
    file_path = tmp_path / "test_countries.csv"
    save_to_csv(sample_dataframe, file_path)
    assert os.path.exists(file_path)
    df = pd.read_csv(file_path)
    assert df.equals(sample_dataframe)

# Negative test: Invalid file path
def test_save_to_csv_invalid_path(sample_dataframe):
    with pytest.raises(OSError):
        save_to_csv(sample_dataframe, "/invalid_path/test_countries.csv")
