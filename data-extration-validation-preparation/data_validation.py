import pandas as pd

# Introducing issues in data
data_with_issues = pd.read_csv('user_data.csv')

# Check for missing values
missing_values = data_with_issues.isnull().sum()
print("Missing Values:\n", missing_values)

# Outlier detection
outliers = data_with_issues[(data_with_issues['age'] > 100) | (data_with_issues['age'] < 0)]
print("Outliers:\n", outliers)

#Overflow
# Basic schema validation
print("Data Types:\n", data_with_issues.dtypes)

# Duplication validation
duplicates = data_with_issues[data_with_issues.duplicated(keep=False)]
if not duplicates.empty:
    print("Duplicate Records:\n", duplicates)
else:
    print("No duplicate records found.")
