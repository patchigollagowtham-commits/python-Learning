import matplotlib.pyplot as plt

# Sample Data
students = ["Rahul", "Priya", "Sai", "Anjali", "Ravi"]
marks = [85, 78, 92, 70, 88]

# ----------------------------
# Line Chart
# ----------------------------
plt.figure(figsize=(6,4))
plt.plot(students, marks, marker='o')
plt.title("Student Marks - Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# ----------------------------
# Bar Chart
# ----------------------------
plt.figure(figsize=(6,4))
plt.bar(students, marks)
plt.title("Student Marks - Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# ----------------------------
# Scatter Plot
# ----------------------------
plt.figure(figsize=(6,4))
plt.scatter(students, marks)
plt.title("Student Marks - Scatter Plot")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
