import numpy as np

npArray = np.array([
        	[29,59,	199,42], # 01-Jun
        	[39,79,	299,22], # 02-Jun
        	[49,89,	399,33], # 03-Jun
        	[59,99,	499,44], # 04-Jun
    ])


# 2d slicing
# array[start_row:end_row, start_col:end_col]

# Mouse => 0
# keyboard => 1
# monitor => 2
# laptop => 3
# print(npArray[0:1,1:3])
# print(npArray[0:3,1:3])

#column selection
print(npArray[:,2]) # [199 299 399 499]
print(npArray[:,1:3])
# [[ 59 199]
#  [ 79 299]
#  [ 89 399]
#  [ 99 499]]

# print(npArray[:,:])



