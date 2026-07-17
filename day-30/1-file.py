# binary => npy

# text => .txt .csv

# np.save => .npy

import numpy as np

array = np.array([10,20,30,40,50],dtype=np.int32)
# file_name, array
np.save("marks",array)

array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
np.save("./data/matrix",array)


