import numpy as np

# 1. Array Creation and Properties
arr = np.random.randint(10, 50, size=(3, 4))
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Size:", arr.size)
print("Data type:", arr.dtype)

# 2. Array Operations
print("Sum of all elements:", arr.sum())
print("Array elements multiplied by 2:\n", arr * 2)
