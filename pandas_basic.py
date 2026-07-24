import pandas as pd

# Load dataset
df = pd.read_csv("student_scores.csv")

# Display dataset
print("Student Dataset")
print(df)

# Number of rows and columns
print("\nRows and Columns:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Dataset information
print("\nDataset Information:")
print(df.info())

# First five rows
print("\nFirst Five Rows:")
print(df.head())

# Last five rows
print("\nLast Five Rows:")
print(df.tail())