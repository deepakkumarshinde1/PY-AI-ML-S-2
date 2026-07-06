import numpy as np

# 1d
ndArray = np.array([10,20,30,40,50,60,70,80,90,100,110,120])
# print(ndArray.shape)

# reshape

# 2d => row,col
ndArray2d = ndArray.reshape(2,6)
# print(ndArray2d)


# 3d => row, col ,depth
ndArray3d = ndArray.reshape(2,2,3)
# print(ndArray3d)

# [
#  [[ 10  20],[ 30  40],[ 50  60] ],
#  [[ 70  80],[ 90 100],[110 120] ]
# ]


#2 => resize
# So basically resize can add or remove 
# the element as per the size and we we can also 
# convert the element to one D, two D or N D.

ndArray = np.array([10,20,30,40,50])
# print(np.resize(ndArray,15))
# print(np.resize(ndArray,3))

# 2d
# print(np.resize(ndArray,(2,2)))

# 3d
# print(np.resize(ndArray,(2,2,4)))

#3 => flatten

ndArray = np.array(
    [  
         [
            [10, 20, 30, 40],
            [50, 10, 20, 30]
        ],
        [
            [40, 50, 10, 20],
            [30, 40, 50, 10]
        ]
    ]
)

oneD = ndArray.flatten()
# create a copy
oneD[5] = 9999


oneD_1 = ndArray.ravel()
#provide view not copy
oneD_1[5] = 111111
# print(oneD)
# print(oneD_1)
# print(ndArray)


# Transpose is commonly used to convert a row to column and column to row.
tArray = np.array([
                    [1,2,3],
                    [4,5,6]
                ])

# print(tArray.transpose())
# [[1 4]
#  [2 5]
#  [3 6]]


# expand_dims
eArray = np.array([
                    10,20,30,40
                ])
expandArray = np.expand_dims(eArray,2) 
print(expandArray)


# squeeze
sArray = np.array([[[1,2,3,4]]])
print(np.squeeze(sArray))