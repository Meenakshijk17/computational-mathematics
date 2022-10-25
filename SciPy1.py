"""Determinant and Inverse"""

import numpy as np
from scipy import linalg 

A = np.array([[1,2,3],[1,5,7],[7,8,9]])      #creating a non-singualar matrix A as an array

d = linalg.det(A)  # determinant of A which is not equal to 0
print("{} has determinant = {} which is not equal to 0. Hence it has an inverse.".format(A,d))

B = linalg.inv(A)      #inverse of A
print("The inverse of {} is {}.".format(A,B))

#Verification
print(A.dot(B))   # should print the identity matrix