# Import required libraries
import pandas as pd

# Load CSV data with error handling
try:
    data = pd.read_csv('user_data.csv')
    # Display extracted data
    print("Extracted Data:")
    print(data.head())  # Works in Jupyter, replace with print() if running in a script
except FileNotFoundError:
    print("Error: The file './user_data.csv' was not found.")
except pd.errors.EmptyDataError:
    print("Error: The CSV file is empty.")
except pd.errors.ParserError:
    print("Error: There was an issue parsing the CSV file.")
