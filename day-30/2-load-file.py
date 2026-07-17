import numpy as np

# The load method needs a proper file extension to load.
array = np.load('./marks.npy')
print(array) # [10 20 30 40 50] => data
print(array.dtype) # int32 => metadata

array = np.load("data/matrix.npy")
print(array) #  data =>
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
print(array.dtype) # int64 => metadata