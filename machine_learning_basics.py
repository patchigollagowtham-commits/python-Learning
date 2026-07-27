
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample Data
hours = [[1], [2], [3], [4], [5], [6], [7], [8]]
marks = [20, 30, 40, 50, 60, 70, 80, 90]

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    hours, marks, test_size=0.25, random_state=42
)

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict marks for test data
predictions = model.predict(X_test)

print("Test Hours:", X_test)
print("Actual Marks:", y_test)
print("Predicted Marks:", predictions)