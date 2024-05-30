class Country:
    """
    A class to represent a Country

    Attributes:
    - id (str): A unique identifier for the country
    - country_name (str): The official name of the country
    - country_code (str): The cioc code of the country
    - currencies (str): Comma-separated currency codes used in the country
    - region (str): The region where the country is located
    - updated_date (str): The date when the data was last updated
    - updated_by (str): The entity that last updated the data
    """

    # Method to initialize a new Country
    def __init__(self, id, country_name, country_code, currencies, region, updated_date, updated_by):
        self.id = id
        self.country_name = country_name
        self.country_code = country_code
        self.currencies = currencies
        self.region = region
        self.updated_date = updated_date
        self.updated_by = updated_by

    # Method to convert the Country object to a dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "country_name": self.country_name,
            "country_code": self.country_code,
            "currencies": self.currencies,
            "region": self.region,
            "updated_date": self.updated_date,
            "updated_by": self.updated_by
        }
