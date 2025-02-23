from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

# Introducing issues in data
data_with_issues = pd.read_csv('user_data.csv')

# Checking for duplicates before removal
duplicates = data_with_issues[data_with_issues.duplicated(keep=False)]
if not duplicates.empty:
    print("Duplicate Records Found:\n", duplicates)
else:
    print("No duplicate records found.")

# Cleaning data: Remove duplicates and fill missing values
data_cleaned = data_with_issues.drop_duplicates()
print("\nData after removing duplicates:\n", data_cleaned)

# Filling missing age values with the median
data_cleaned['age'].fillna(data_cleaned['age'].median(), inplace=True)

# Normalize the age feature
scaler = MinMaxScaler()
data_cleaned['age_scaled'] = scaler.fit_transform(data_cleaned[['age']])

# Splitting data into train and test sets
train, test = train_test_split(data_cleaned, test_size=0.2, random_state=42)

print("\nTraining Data:")
print(train)
print("\nTesting Data:")
print(test)
