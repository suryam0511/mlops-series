# Import required libraries
import pandas as pd

# Load CSV data
data = pd.read_csv('./user_data.csv')

# Display extracted data
print("Extracted Data:")
data.head()