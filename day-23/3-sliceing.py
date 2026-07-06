import numpy as np

npArray = np.array([60,20,30,40,50,60,70,80,90,100])
# array[start:end:step]
# start => Including.
# end => Excluding.
# step => How many steps to jump.

print(npArray[1:7])
print(npArray[:7])
print(npArray[7:])
print(npArray[:])
print(npArray[::3])
