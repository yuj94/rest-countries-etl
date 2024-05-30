import requests

def fetch_countries(url):

    """
    Method used to fetch the country data from the API endpoint
    
    Args:
        url (str): string of the API endpoint
    
    Returns:
        list: A list of the country data in JSON format
    """

    response = requests.get(url)
    # If successful, nothing happens. If the request failed, will throw HTTPError
    response.raise_for_status()
    return response.json()
