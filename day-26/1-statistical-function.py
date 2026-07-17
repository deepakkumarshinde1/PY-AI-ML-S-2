import numpy as np

ndArray = np.array([
    12,
    33,
    21,
    56,
    61,
    77,
    10
])

print("The sum of weekly sell product is:",np.sum(ndArray))

ndArray = np.array([
    [5,0,4],
    [1,2,0],
    [5,7,3],
    [5,6,2],
    [6,1,3],
    [7,7,6],
    [1,0,0]
])
# axis => 0 vertical => cols
# axis => 1  horizontal => rows
print(np.sum(ndArray,axis=1))
print(np.sum(ndArray,axis=0))

# min is used to find out minimum number from a given array.
# max is used to find out a bigger number, largest number from a given area.
ndArray = np.array([
    12,
    33,
    21,
    56,
    61,
    77,
    10
])

print("min value ",np.min(ndArray))
print("min value index",np.argmin(ndArray))
print("max value ",np.max(ndArray))
print("max value index",np.argmax(ndArray))

ndArray = np.array([
    [5,0,4],
    [1,2,0],
    [5,7,3],
    [5,6,2],
    [6,1,3],
    [7,7,6],
    [1,0,0]
])

print("min value for each row ",np.min(ndArray,axis=1))
print("min value for each col ",np.min(ndArray,axis=0))

print("max value for each row ",np.max(ndArray,axis=1))
print("max value for each col ",np.max(ndArray,axis=0))



# mean => Average of your array
# median => It will provide a middle value of a array.
ndArray = np.array([2,4,10,8,1000,10])

# result = np.sum(ndArray) / len(ndArray)
print(np.mean(ndArray))
print(np.median(ndArray))


# standard deviation measures how spread out data is.
# If a number is small, it is stable. 
# If the number isis large, it is Highly fluctuating.

productSellRecord = np.array([10,2,50,12,7,90,0])
productSellRecord = np.array([50,51,52,49,50,55,51])
print(np.std(productSellRecord))


# percentile is a measure used in statistics indicating the value 
# below which a given percentage of observations in a group of observations fall.
# For example, the 20th percentile is the value (or score) below 
# which 20 percent of the observations may be found.
studentMarksForPython = np.array([30,35,40,50,60,65,70,80,90,95,100])
# 200 student
print(np.percentile(studentMarksForPython,50))

