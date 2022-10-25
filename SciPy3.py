"""Eigen Values and Eigen Vectors"""

import numpy as np
from scipy import linalg 

A = np.array([[1, 2], [3, 4]])

val, vec = linalg.eig(A)

val1, val2 = val   # the eigen values
print("The eigen values of the matrix {} are : {},{}.".format(A,val1,val2))

vec1 = vec[:, 0] # first eigen vector
vec2 = vec[:, 1] # second eigen vector
print("The corresponding eigen vectors are : ",vec1,vec2)

#Verification
print(linalg.norm(A.dot(vec1) - val1*vec1)) # should print 0
print(linalg.norm(A.dot(vec2) - val2*vec2)) # should print 0