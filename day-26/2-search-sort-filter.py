import numpy as np

ndArray = np.array([12,33,21,56,61,77,10])

# sort
# print(np.sort(ndArray))

# array = np.sort(ndArray)[::-1]
# print(array)


# where => return index []
condArray = np.where(ndArray > 25)

print(ndArray[condArray])

# boolean filter
condBooleanArray = ndArray > 25
print(ndArray[condBooleanArray])