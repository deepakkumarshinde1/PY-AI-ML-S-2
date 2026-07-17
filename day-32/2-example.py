import numpy as np
patients = np.array([
"P101",
"P102",
"P103",
"P104",
"P105"
])
temperature = np.array([
    [36.8,37.2,37.0,36.9],
    [38.5,39.0,38.7,38.2],
    [36.5,36.6,36.8,36.7],
    [39.1,39.3,39.0,38.8],
    [37.1,37.0,37.2,37.3]
])

# Calculate average temperature of every patient.
result = np.mean(temperature,axis=1)
print("average temperature of every patient is ", result)

# Find patients whose average temperature exceeds 38°C.
index = np.where(result > 38)
print("patients whose average temperature exceeds 38°C is ",patients[index])

# Find highest temperature recorded.
result = np.max(temperature)
print("highest temperature recorded is ",result)

# Find patient having highest temperature.
value = np.max(temperature)
row,col = np.where(temperature == value)
print("patient having highest temperature is ",patients[row[0]])

# Find minimum temperature.
value = np.min(temperature)
row,col = np.where(temperature == value)
print("patient having minimum temperature is ",patients[row[0]])

# Calculate overall hospital average temperature.
avg = np.mean(temperature)
print("overall hospital average temperature is ",avg)

# Display only normal patients (below 37.5°C average).
result = np.mean(temperature , axis=1)
index= np.where(result < 37.5)
print("only normal patients as per temp is ",patients[index])

# Find which reading of Patient P104 was maximum.
result = np.max(temperature[3])
print("reading of Patient P104 was maximum for",result," temp")

#  Calculate variance of temperatures.
print(np.var(temperature))
print(np.std(temperature))