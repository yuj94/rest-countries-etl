import pandas as pd
#import uuid
from datetime import datetime
from models import Country

def transform_countries(countries):

    """
    Method used to transform the country data into the desired output
    
    Args:
        countries (list): list of the country data
    
    Returns:
        pd.DataFrame: A DataFrame object of the transformed data
    """

    # Creates an empty list
    records = []

    # Loops the country in the countries list and sets the specified country data as a variables and creates a new country object to save to the list
    for country in countries:

        # Extract the two-letter country code if available. Code ISO 3166-1 alpha-2 (cca2) is a unique identifier for a country.
        # '.get()' method is used to access 'cca2', otherwise set an empty string as a default value
        # id derived from cca2
        id = country.get("cca2", "")

        # Extract the official name of the country if available
        # the first '.get()' method is used to access 'name' which is expected to be a dictionary
        # the next '.get()' method is used to access 'official', otherwise set an empty string as a default value
        # country_name derived from name.official
        country_name = country.get("name", {}).get("official", "")

        # Extract the country code if available
        # '.get()' method is used to access 'cioc', otherwise set an empty string as a default value
        # country_code derived from cioc
        country_code = country.get("cioc", "")

        # Extract the country code if available
        # '.get()' method is used to access 'currencies' which is expected to be a dictionary
        # '.keys()' retrieves the currency codes which are the keys of the 'currencies' dictionary
        # ','.join() combines these keys into a single string with commas as separators
        # currencies derived from currency codes, delimited by commas
        currencies = ",".join(country.get("currencies", {}).keys())

        # Extract the region if available
        # '.get()' method is used to access 'region', otherwise set an empty string as a default value
        # region derived from region
        region = country.get("region", "")

        # Create a Country object of country_obj and set its attributes based in the data set above
        country_obj = Country(
            #id = str(uuid.uuid4()), #another way for a unique modifier
            id = id,
            country_name = country_name,
            country_code = country_code,
            currencies = currencies,
            region = region,
            updated_date = datetime.now().strftime('%Y-%m-%d'),
            updated_by = "system"
        )

        # Convert the Country object of country_obj to a dictionary and add to the records list
        records.append(country_obj.to_dict())

    return pd.DataFrame(records)
