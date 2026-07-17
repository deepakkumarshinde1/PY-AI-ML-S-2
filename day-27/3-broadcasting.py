import numpy as np

npArray = np.array([ 100,  200,  300,  400])

# Broadcasting is Numpy's ability 
# to perform operations on arrays of different shape 
# by automatically expanding the small array.

finalProductPrice = npArray + 40
# finalProductPrice = npArray + [40]

# [40 40 40 40]

# print(finalProductPrice)

npArray1= np.array([ 100,  200,  300,  400])
npArray2= np.array([ 4400,  5500])
# ValueError: operands could not be broadcast 
# together with shapes (4,) (2,) 
# result = npArray1 + npArray2
# print(result)

# So if first is an array and if we try to broadcast with a single value, it works.
# So if your 1st array has 4 value and if the 2nd array has only 1 value, still the broadcasting can be done.
# If your 1st array has 4 values and if the 2nd array has 2 values, then you will not able to broadcast because its shape changes.


# 2D array broadcasting
# type-1
npArray1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ])
# 3 rows ,3 col

npArray2 = np.array([
    [10]
 ])

# print(npArray1 + npArray2)
# npArray2
#   [
#     [10,10,10],
#     [10,10,10],
#     [10,10,10]
#  ]
# 1 row 1 col






# type -2
npArray1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ])
# 3 rows ,3 col

npArray2 = np.array([
    [10],
    [20],
    [30]
 ])

# print(npArray1 + npArray2)
# npArray2
#   [
#     [10,10,10],
#     [20,20,20],
#     [30,30,30]
#  ]
# 3 row 1 col





# type 3
npArray1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
 ])
# 3 rows ,3 col

npArray2 = np.array([
    [10,20,30]
 ])

print(npArray1 + npArray2)
# npArray2
#   [
#     [10,20,30],
#     [10,20,30],
#     [10,20,30],
#  ]
# 1 row 3 col
