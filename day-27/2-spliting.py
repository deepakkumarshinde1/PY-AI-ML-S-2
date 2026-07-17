import numpy as np

npArray = np.array([ 10,  20,  30,  40, 100, 200, 300, 400,500])
# np.split(array,number of rows)
# print(np.split(npArray,3))
# [
#         array([10, 20, 30]),
#         array([ 40, 100, 200]), 
#         array([300, 400, 500])
# ]
# print(np.split(npArray,9))
# [
#     array([10]), 
#     array([20]), 
#     array([30]), 
#     array([40]), 
#     array([100]), 
#     array([200]), 
#     array([300]), 
#     array([400]), 
#     array([500])
# ]

# print(np.split(npArray,7))
# ValueError: array split does not result in an equal division
npArray = np.array([ 
            [10,  20,  30, 35],  
            [40, 100, 200, 250],
            [300, 400,500, 560],
            [1000,2000,3000,4000]
        ])

print(np.hsplit(npArray,2))
# [array([[  10,   20],[  40,  100],[ 300,  400],[1000, 2000]]),
# array([[  30,   35],[ 200,  250], [ 500,  560],[3000, 4000]])]

print(np.vsplit(npArray,2))
# [array([[ 10,  20,  30,  35],[ 40, 100, 200, 250]]), 
#  array([[ 300,  400,  500,  560],[1000, 2000, 3000, 4000]])]