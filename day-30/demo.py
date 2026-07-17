import numpy as np

#            0.  1.   2.    3.   4
my_nums = [100, 200, 300, 400, 500]

# print(my_nums)
# 0 to 2
# start : end
# start, end - 1 => print
print(my_nums[ 3 : 6])
# print(my_nums[2: ])


# _list = [
#             [1,2,3], 
#             [1,3,4],
#             [5, 9, 8]
#         ]

# print(_list[2][1])

# dimension: m = rows x n cols
nums = np.array([
            [1,2,3], 
            [1,3,4], 
            [5,9,8],
            [11, 12, 13]
        ])
# [
# [9, 8]
# [12, 13]
# ]

# print("----------")
# print(nums[2, 1])


# # select a row number 3
# print("****")
# # print(nums[2])
# # print(nums[3])

# # 1, 5 => 1, 2, 3, 4
# # slicing (start, end)
# # inclusive
# # exclusive
print(nums[2:4, 1:3])