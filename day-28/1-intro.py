
# Algebra is basically a mathematical branch which deals with numbers and symbols.
# x + 5 = 7
# what is x => 2
# x = 7 -5
# x= 2

import numpy as np
# leaner algebra 
# Numbers => scale i.e single number
np.array(10)

# vector
np.array([1,2,3])

# Matrices
np.array(
    [[1,2,3],
     [4,5,6]])

# Equations

# print(npArray1 + npArray2)
# print(npArray1 - npArray2)
# print(npArray1 / npArray2)

npArray1 = np.array([
    [1,2],
    [3,4]
])#a

npArray2 = np.array([
    [5,6],
    [7,8]
])#b
# print(npArray1 * npArray2)
# ar1c1*br1c1 ar1c2*br1c2
# ar2c1*br2c1 ar2c2*br2c2

# Matrix multiplication.
# print(npArray1 @ npArray2)
# print(np.dot(npArray1 , npArray2))
# print(np.matmul(npArray1 , npArray2))

# determinant.
npArray2 = np.array([
    [5,6],
    [7,8]
])#b
# [ a b 
#   c d ]

# print(np.linalg.det(npArray2))
# ad - bc = det
# -2

# print(np.eye(3,dtype=int))



npArray1 = np.array([
    [1,2],
    [3,4]
])

inverseArray = np.linalg.inv(npArray1)
print(inverseArray)

print(np.dot(npArray1,inverseArray))

# Transformation.

npArray1 = np.array([
    [1,2],
    [3,4]
])

print(np.transpose(npArray1))
print(npArray1.T)