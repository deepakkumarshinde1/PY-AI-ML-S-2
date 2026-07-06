import numpy as np
# array 1d
npArray = np.array([299,399,599,799,1999,2999])
# array[index]
print(npArray[5])

# 2d
npArray = np.array([
        [299,399,499,599],# Mouse.
        [599,799,899,999], # Keyboard.
        [1999,2999,3999,4999] # Monitor.
    ])
# array[row,col]
print(npArray[0,2])


