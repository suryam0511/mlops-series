from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import pandas as pd

# Load CSV data
data = pd.read_csv('./user_data.csv')

# Cleaning data: Remove duplicates and fill missing values
data_cleaned = data.drop_duplicates()
data_cleaned['age'].fillna(data_cleaned['age'].median(), inplace=True)

# Normalize the age feature
scaler = MinMaxScaler()
data_cleaned['age_scaled'] = scaler.fit_transform(data_cleaned[['age']])

# Splitting data into train and test sets
train, test = train_test_split(data_cleaned, test_size=0.2, random_state=42)

print("Training Data:")
print(train)
print("Testing Data:")
print(test)