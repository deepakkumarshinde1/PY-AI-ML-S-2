import numpy as np

_list = [1,2,3]
npArray = np.array([1,2,3])
print(_list * 2) # [1, 2, 3, 1, 2, 3]
print(npArray*2) # [2 4 6]

# scaler => 0D
npArray = np.array(5)

# Vector => 1d
npArray = np.array([1,2,3,4])

# Matrix => 2d
npArray = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# Tensor 3d ... nd
npArray = np.array([
    [
        [1,2,3],
        [2,3,4],
        [1,2,1]
    ],
])


array1 = np.array([
            [ 1,5],
            [7,3]
        ])
array2 = np.array([
        [12,-1],
        [0,9]
    ])

array1 = array1 + array2
print(array1)