import numpy as np

# rand
array = np.random.rand() # single
array = np.random.rand(5) # 1d
array = np.random.rand(5,3) # 1d
# print(array)

# randint (low , high, size(r,col))
# array = np.random.randint(50000,99999)
array = np.random.randint(18,40,size=(5,10))
# print(array)

# randn
array = np.random.randn()
array = 170 + (np.random.randn(10,3) * 10)
# print(array)

# choice

# [SND MET JIT NDMVP GGS KKW]
# [1 2 3 4 5 6]
array = np.array([1, 2, 3, 4, 5, 6])
array = np.random.choice(array,size=1,replace=False,p=[0.05, 0.1 , 0.4, 0.3, 0.1,0.05 ]) 
# print(array)


# Shuffling
# So in 2 D array, shuffling works with only axis 0.
array = np.array([ "Saish", "Anisha", "Anuja", "Kartik", "Pranav" ,"Om"])
np.random.shuffle(array)
# print(array)

np.random.seed(100)
array = np.random.randint(10,20,size=5)
print(array)
