import logging
#import schedule
#import time
# Only importing the specific function, not the whole module
from fetch_data import fetch_countries
from transform_data import transform_countries
from save_data import save_to_csv

# Configure the logging system to display logs with level of 'INFO' or higher
logging.basicConfig(level=logging.INFO)
# Creates a logger named according to the module
logger = logging.getLogger(__name__)

SOURCE_URL = "https://restcountries.com/v3.1/all"
OUTPUT_LOCATION = "output/countries.csv"

# Main function to execute the data pipeline for data fetching, transformation, and saving processes
def run_pipeline():
    logger.info("Starting Data Pipeline")

    try:
        logger.info("Fetching country data")
        countries = fetch_countries(SOURCE_URL)

        logger.info("Transforming country data")
        transformed_countries = transform_countries(countries)

        logger.info("Saving transformed data to CSV")
        save_to_csv(transformed_countries, OUTPUT_LOCATION)
    except Exception as e:
        # f signifies an f-string, which stands for formatted string literal
        logger.error(f"An error occurred: {e}")

    logger.info("Data Pipeline completed successfully")

# Checks if the script is being run as the main program or imported
if __name__ == "__main__":

    # If you want to run this locally, uncomment the line 39 - 40 and comment out lines 42 - 49 and 2 - 3
    run_pipeline()

    # # If ypu want to schedule the pipeline to run every day at midnight, uncomment out lines 42 - 49 and 2 - 3 and comment out line 39 - 40
    # schedule.every().day.at("00:00").do(run_pipeline)

    # logger.info("Starting scheduler")
    # # This loop continuously checks for scheduled tasks to run any pending jobs and wait 1 second between checks
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
