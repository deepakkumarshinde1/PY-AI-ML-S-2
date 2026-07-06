import numpy as np

# 8 bit === 1 byte
npArray = np.array([1,2,3])

# print(np.__version__)
# print(type(npArray)) # <class 'numpy.ndarray'>
# print("dim is : ",npArray.ndim) # dim is :  1
npArray = np.array(4)
# print("dim is : ",npArray.ndim) # dim is :  0

npArray = np.array([ [], [] ])
# print("dim is : ",npArray.ndim) # dim is :  2

npArray = np.array([ [
    []
], [
    []
] ])
# print("dim is : ",npArray.ndim) # dim is :  3


ndArray = np.array([
    [1,2,3],
    [4,5,6]
])

print(ndArray.size)
print(ndArray.dtype)

# int8 => 8 bit
# int16 => 16 bit
# int32 => 32 bit
# int64 => 64 bit

# float32 => decimal
# float64 => Heigh Precision decimal.

# bool => true,false

print(ndArray.size) # total element
print(ndArray.itemsize) # only element size ( byte )
print(ndArray.nbytes) # total + single_element_size


