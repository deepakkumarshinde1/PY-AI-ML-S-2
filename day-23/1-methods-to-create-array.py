import numpy as np

# 2d
npArray = np.zeros((5,5),dtype=int)
# print(npArray)

# 1d
npArray = np.zeros(5,dtype=int)
# print(npArray)


# 2d
npArray = np.ones((5,5),dtype=int)
# print(npArray)

# 1d
npArray = np.ones(5,dtype=int)
# print(npArray)


# 2d
npArray = np.full((5,5),5.5)
# print(npArray)

# 1d
npArray = np.full(5,5.5)
# print(npArray)

npArray = np.eye(5,5,dtype=int)
# print(npArray)

npArray = np.arange(11) # [ 0  1  2  3  4  5  6  7  8  9 10]
npArray = np.arange(3,11) # [ 3  4  5  6  7  8  9 10]
npArray = np.arange(3,11,2) # [3 5 7 9]
# print(npArray)

# 0 1 5 parts
# [0 0.25 0.5 0.75 1]
npArray = np.linspace(0,1,5) # [0.   0.25 0.5  0.75 1.  ]
npArray = np.linspace(1,10,5) # [ 1.    3.25  5.5   7.75 10.  ]
npArray = np.linspace(1,10,10,dtype=int) # [ 1  2  3  4  5  6  7  8  9 10]
print(npArray)


