import numpy as np

npArray = np.zeros((3,4),dtype=int)
print(npArray)
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]


npArray = np.ones((3,4),dtype=int)
print(npArray)
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

npArray = np.full((4,4),2,dtype=int)
print(npArray)
# [[2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]
#  [2 2 2 2]]