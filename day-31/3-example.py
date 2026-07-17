import numpy as np
# create numpy array ( load )
array = np.loadtxt(
    "example-3.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1,2,3,4)
    ,dtype=int
)


print(array)

# display shape or array
print("shape", array.shape)
# display size
print("size", array.size)
# display dimension
print("dimension", array.ndim)

print("details  3rd Patient is ",array[2])

# only blood sugar levels of all patients.
print("blood sugar levels of all patients.",array[:,3])

# print age & weight of all patents
print("age & weight of all patents",array[:,0:2])


# print heart rate of all patients
print("heart rate of all patients",array[:,2])


# inc and print weight of all patents by 2 kg
print("inc weight of all patents is ",array[:,1] + 2)

# print avg age 
print("avg age is", np.mean(array[:,0]))

# print high sugar level
print("high sugar level is ", np.max(array[:,3]))

# 50th percentile for sugar level
print("50th percentile for sugar level ", np.percentile(array[:,3],50))

# all values > then 120 for sugar level
array1 = array[:,3]
print(array1[array1 > 120])
