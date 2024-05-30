# REST Countries ETL Project

_Duration: 12 hours_

## Overview

A data pipeline system designed to interact with the public [REST Countries](https://restcountries.com/v3.1/all) API. The system fetches data, performs necessary transformations to structure the data according to a specified schema, and saves the processed data as a CSV file to a desired location. For this project, we will save the CSV file to a folder called `output` at the root directory.

So why Python? Python has a large set of libraries and frameworks that can handle different aspects of the ETL process. These processes include data extraction, manipulation, processing, and loading. Pandas is one of these libraries. It provides powerful tools for handling structured data with its intuitive DataFrame objects. Its ease of use make it an essential tool for data engineers and analysts working on ETL tasks.

Note: This was developed on macOS. Setup may vary on your operating system.

## Requirements

- [Python 3+](https://www.python.org/downloads/)
- Code Editor
    - Recommended to use [Visual Studio Code](https://code.visualstudio.com/download)
        - Recommended Extensions:
            - [Python](vscode:extension/ms-python.python)
            - [Code Spell Check](vscode:extension/streetsidesoftware.code-spell-checker)
            - [Rainbow CSV](vscode:extension/mechatroner.rainbow-csv)
- Recommended: [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- `requests` [Library](https://pypi.org/project/requests/)
- `pandas` [Library](https://pandas.pydata.org/)
- `schedule` [Library](https://schedule.readthedocs.io/en/stable/)
- `pytest` [Framework](https://docs.pytest.org/en/8.2.x/)
- `coverage` [Tool](https://coverage.readthedocs.io/en/7.5.3/)

## Project Structure

```
rest-countries-etl/
├── main.py
├── fetch_data.py
├── transform_data.py
├── save_data.py
├── models.py
├── requirements.txt
├── README.md
├── tests/
│   └── test_rest_countries_etl.py
└── output/
    └── countries.csv
```

1. Data Ingestion:
    - Module: fetch_data.py
    - Function: fetch_countries(url)
    - Purpose: Method used to fetch the country data from the API endpoint

2. Data Transformation:
    - Module: transform_data.py
    - Function: transform_countries(countries)
    - Purpose: Method used to transform the country data into the desired output

3. Data Storage:
    - Module: save_data.py
    - Function: save_to_csv(data, file_path)
    - Purpose: Method used saved the transformed data to a CSV file to your desired output location

4.  Data Model:
    - Module: models.py
    - Class: Country
    - Purpose: A class to represent a Country

5. Pipeline Execution:
    - Module: main.py
    - Function: run_pipeline()
    - Purpose: Main function to execute the data pipeline for data fetching, transformation, and saving processes
    - Scheduling: Uses `schedule` library to run the pipeline at specified intervals

## Setup

1. Please look at the [Requirements](#requirements) section above to get started. Stay in the root directory.

2. Create a virtual environment:
    ```sh
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```

4. Install the dependencies:
    ```sh
    python3 -m pip install -r requirements.txt
    ```

5. Create an `output` folder at the root directory of the project
    ```
    rest-countries-etl/
    └── output/
    ```

6. Run the data pipeline:

    ```sh
    python3 main.py
    ```

## Running Tests

1. Please look at the [Requirements](#requirements) section above to get started. You can skip Steps 1 through 4 if you completed this in [Setup](#setup). Stay in the root directory.

2. Create a virtual environment:
    ```sh
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    ```sh
    source .venv/bin/activate
    ```

4. Install the dependencies:
    ```sh
    python3 -m pip install -r requirements.txt
    ```

5. Run the tests:
    ```sh
    python3 -m pytest tests/
    ```

6. Run the tests with coverage:
    ```sh
    coverage run -m pytest tests/
    ```

7. Generate a coverage report:
    ```sh
    coverage report
    ```

8. Generate a more detailed HTML coverage report:
    ```sh
    coverage html
    ```

9. Open the HTML generated report:
    ```sh
    open htmlcov/index.html
    ```

## Example

#### Sample Country:

<details>
    <summary>See JSON example</summary>


    [
        {
            "name": {
            "common": "Moldova",
            "official": "Republic of Moldova",
            "nativeName": {
                "ron": {
                "official": "Republica Moldova",
                "common": "Moldova"
                }
            }
            },
            "tld": [
            ".md"
            ],
            "cca2": "MD",
            "ccn3": "498",
            "cca3": "MDA",
            "cioc": "MDA",
            "independent": true,
            "status": "officially-assigned",
            "unMember": true,
            "currencies": {
            "MDL": {
                "name": "Moldovan leu",
                "symbol": "L"
            }
            },
            "idd": {
            "root": "+3",
            "suffixes": [
                "73"
            ]
            },
            "capital": [
            "Chișinău"
            ],
            "altSpellings": [
            "MD",
            "Moldova, Republic of",
            "Republic of Moldova",
            "Republica Moldova"
            ],
            "region": "Europe",
            "subregion": "Eastern Europe",
            "languages": {
            "ron": "Romanian"
            },
            "translations": {
            "ara": {
                "official": "جمهورية مولدوڤا",
                "common": "مولدوڤا"
            },
            "bre": {
                "official": "Republik Moldova",
                "common": "Moldova"
            },
            "ces": {
                "official": "Moldavská republika",
                "common": "Moldavsko"
            },
            "cym": {
                "official": "Republic of Moldova",
                "common": "Moldova"
            },
            "deu": {
                "official": "Republik Moldau",
                "common": "Moldawien"
            },
            "est": {
                "official": "Moldova Vabariik",
                "common": "Moldova"
            },
            "fin": {
                "official": "Moldovan tasavalta",
                "common": "Moldova"
            },
            "fra": {
                "official": "République de Moldavie",
                "common": "Moldavie"
            },
            "hrv": {
                "official": "Moldavija",
                "common": "Moldova"
            },
            "hun": {
                "official": "Moldovai Köztársaság",
                "common": "Moldova"
            },
            "ita": {
                "official": "Repubblica di Moldova",
                "common": "Moldavia"
            },
            "jpn": {
                "official": "モルドバ共和国",
                "common": "モルドバ共和国"
            },
            "kor": {
                "official": "몰도바 공화국",
                "common": "몰도바"
            },
            "nld": {
                "official": "Republiek Moldavië",
                "common": "Moldavië"
            },
            "per": {
                "official": "جمهوری مولداوی",
                "common": "مولداوی"
            },
            "pol": {
                "official": "Republika Mołdawii",
                "common": "Mołdawia"
            },
            "por": {
                "official": "República da Moldávia",
                "common": "Moldávia"
            },
            "rus": {
                "official": "Молдова",
                "common": "Молдавия"
            },
            "slk": {
                "official": "Moldavská republika",
                "common": "Moldavsko"
            },
            "spa": {
                "official": "República de Moldova",
                "common": "Moldavia"
            },
            "srp": {
                "official": "Република Молдавија",
                "common": "Молдавија"
            },
            "swe": {
                "official": "Republiken Moldavien",
                "common": "Moldavien"
            },
            "tur": {
                "official": "Moldova Cumhuriyeti",
                "common": "Moldova"
            },
            "urd": {
                "official": "جمہوریہ مالدووا",
                "common": "مالدووا"
            },
            "zho": {
                "official": "摩尔多瓦共和国",
                "common": "摩尔多瓦"
            }
            },
            "latlng": [47, 29],
            "landlocked": true,
            "borders": [
            "ROU",
            "UKR"
            ],
            "area": 33846,
            "demonyms": {
            "eng": {
                "f": "Moldovan",
                "m": "Moldovan"
            },
            "fra": {
                "f": "Moldave",
                "m": "Moldave"
            }
            },
            "flag": "🇲🇩",
            "maps": {
            "googleMaps": "https://goo.gl/maps/JjmyUuULujnDeFPf7",
            "openStreetMaps": "https://www.openstreetmap.org/relation/58974"
            },
            "population": 2617820,
            "gini": {
            "2018": 25.7
            },
            "fifa": "MDA",
            "car": {
            "signs": [
                "MD"
            ],
            "side": "right"
            },
            "timezones": [
            "UTC+02:00"
            ],
            "continents": [
            "Europe"
            ],
            "flags": {
            "png": "https://flagcdn.com/w320/md.png",
            "svg": "https://flagcdn.com/md.svg",
            "alt": "The flag of Moldova is composed of three equal vertical bands of blue, yellow and red, with the national coat of arms centered in the yellow band."
            },
            "coatOfArms": {
            "png": "https://mainfacts.com/media/images/coats_of_arms/md.png",
            "svg": "https://mainfacts.com/media/images/coats_of_arms/md.svg"
            },
            "startOfWeek": "monday",
            "capitalInfo": {
            "latlng": [47.01, 28.9]
            },
            "postalCode": {
            "format": "MD-####",
            "regex": "^(?:MD)*(\\d{4})$"
            }
        }
    ]
</details>

#### Sample Output:

| id    | country_name          | country_code  | currencies    | region    | updated_date  | updated_by    |
| :---: | :---                  | :---:         | :---:         | :---:     | :---          | :---          |
| MD    | Republic of Moldova   | MDA           | MDL           | Europe    | 2024-05-29    | system        |

## Assumptions

- The API endpoint is fixed to [https://restcountries.com/v3.1/all](https://restcountries.com/v3.1/all)
- The desired location is fixed to the folder `output`
- The pipeline is scheduled to run daily at midnight
- The id column can be derived from cca2

## Next Steps

- Have the desired transformation be more dynamic with the use of configuration files
- Implement more robust error handling and retries to manage potential issues
- Enhance the transformation logic for more complex schemas
- Add support for different output formats (e.g., JSON, database)
- Containerize the application for consistent deployments across different environments
- Additional unit and integration tests
- Use an ETL tool instead for production-grade product as this pipeline scales
