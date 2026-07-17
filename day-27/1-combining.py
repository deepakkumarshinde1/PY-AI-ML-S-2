import numpy as np

npArray1 = np.array([10,20,30,40])
npArray2 = np.array([100,200,300,400])

newArray = np.concatenate((npArray1,npArray2))
# print(newArray)
# [ 10  20  30  40 100 200 300 400]

npArray1 = np.array([
                [10,20],
                [30,40]
        ])
npArray2 = np.array([
                    [100,200],
                    [300,400]
                    ])
# axis-0 v => row wise
# axis-1 h => col wise
newArray = np.concatenate((npArray1,npArray2),axis=0)
# print(newArray)
# [[ 10  20 100 200]
#  [ 30  40 300 400]]
# [10,20],
# [30,40],
# [100,200],
# [300,400]

# stack create a new axis for 1d array
npArray1 = np.array([10,20,30,40])
npArray2 = np.array([100,200,300,400])
# create new axis
newArray = np.stack((npArray1,npArray2),axis=1)
# print(newArray)

# newArray = np.hstack((npArray1,npArray2))
# [ 10  20  30  40 100 200 300 400]
# newArray = np.vstack((npArray1,npArray2))
# [[ 10  20  30  40]
# [100 200 300 400]]
print(newArray)






