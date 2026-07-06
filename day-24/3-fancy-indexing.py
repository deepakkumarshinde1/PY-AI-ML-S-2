import numpy as np

npArray = np.array([
        	29,59,	199,42,
        	39,79,	299,22,
        	49,89,	399,33,
        	59,99,	499,44,
    ])

# [ 29  59 199  42  39  79 299  22  49  89 399  33  59  99 499  44]
indexList = [3,5,9]
# print(npArray[indexList])

# cond => indexList => extract data
# np.where(cond)

indexList = np.where(npArray > 80)
print(npArray[indexList])