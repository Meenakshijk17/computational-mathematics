"""Solving Linear System"""

import numpy as np
from scipy import linalg 

A = np.array([[1, 2], [3, 4]]) # coefficient matrix 
b = np.array([[5], [6]])   # data matrix

# Method 1
x1 = linalg.inv(A).dot(b) # solution
print(x1)
# Verification 
print(A.dot(x1) - b) # should print the zero matrix

# Method 2
x2 = linalg.solve(A, b)   # solution
print(x2)
# Verification
print(A.dot(x2) - b)  # should print the zero matrix