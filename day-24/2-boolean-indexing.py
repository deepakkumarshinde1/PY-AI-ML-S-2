import numpy as np

npArray = np.array([
        	[29,59,	199,42], # 01-Jun
        	[39,79,	299,22], # 02-Jun
        	[49,89,	399,33], # 03-Jun
        	[59,99,	499,44], # 04-Jun
    ])

firstOfJune = npArray[0]
cond = (firstOfJune > 42)
# print( firstOfJune[cond] ) #[ 59 199]

# multiple conditions
data = npArray[:,1:3]
cond = (data > 89) & (data < 399)
print(data[cond])
# [199 299  99]