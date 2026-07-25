
import pandas as pd

# Load the dataset
df = pd.read_csv("student_data.csv")

print("Original Dataset")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing values with 0
df.fillna(0, inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nCleaned Dataset")
print(df)

# Display statistics
print("\nDataset Statistics")
print(df.describe())

# Save cleaned dataset
df.to_csv("cleaned_student_data.csv", index=False)

print("\nCleaned dataset saved as cleaned_student_data.csv")