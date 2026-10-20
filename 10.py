import numpy as np

arr = np.array([1, 2, 3, 4])

arr = np.append(arr, 5)
print(arr)  # Output: [1 2 3 4 5]

# Reverse using np.flip
reversed_arr = np.flip(arr)

print(reversed_arr)  # Output: [5 4 3 2 1]
