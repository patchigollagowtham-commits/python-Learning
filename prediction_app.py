import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 30, 40, 50, 60, 70, 80, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and Target
X = df[["Hours"]]
y = df["Marks"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Get user input
hours = float(input("Enter study hours: "))

# Predict score
predicted_score = model.predict([[hours]])

print(f"Predicted Score: {predicted_score[0]:.2f}")