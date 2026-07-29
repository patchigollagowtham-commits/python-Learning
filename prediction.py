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

# Predict scores for new study hours
new_hours = [[2.5], [5.5], [9]]

predicted_marks = model.predict(new_hours)

print("Predictions:")
for hours, marks in zip(new_hours, predicted_marks):
    print(f"Study Hours: {hours[0]} -> Predicted Marks: {marks:.2f}")