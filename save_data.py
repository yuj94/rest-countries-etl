def save_to_csv(data, file_path):

    """
    Method used saved the transformed data to a CSV file to your desired output location
    
    Args:
        data (pd.DataFrame): The transformed data
        file_path (str): The path to save the CSV file
    """

    # Method provided from the panda Library to save the DataFrame object to a CSV file to the desired location without saving the index
    data.to_csv(file_path, index=False)
