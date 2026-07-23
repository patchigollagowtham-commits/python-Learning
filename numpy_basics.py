import numpy as np

# Create Array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)

# Indexing
print("First Element:", arr[0])
print("Last Element:", arr[-1])

# Slicing
print("Sliced Array:", arr[1:4])

# Mathematical Operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# Calculations
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# 2D Array
matrix = np.array([[1,2,3],[4,5,6]])

print(matrix)

print("Element:", matrix[1,2])