import pandas as pd
import numpy as np


print(pd.__version__)

# 1d => vector => Series
# series is a one-dimensional labelled array of data sets.
# from list
students = [40,50,33,77]
index = ["A","B","C","D"]
pdData = pd.Series(students,index=index)

# from dictionary
students = {
    "A":40,
    "B":50,
    "C":33,
    "D":77
}

pdData = pd.Series(students)

# numpy
npArray = np.array([10,20,30,40])
pdData = pd.Series(npArray)

print(pdData)
print(pdData.values)
print(pdData.index)
print(pdData.dtype)
print(pdData.ndim)
print(len(pdData))

# 2d => matrix => dataFrame
# 3d => tensor => tensor