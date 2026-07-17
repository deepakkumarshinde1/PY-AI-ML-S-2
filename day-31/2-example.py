# We have a dataset available in emp_details.csv
# find
# 1. Average salary
# 2. emp's amount  with highest salary
# 3. emp's amount with lowest salary
# 4. give every emp 1000 hike
# 5. total emp salary
import numpy as np

array = np.loadtxt('emp_details.csv',
                   delimiter=',',
                   skiprows=1,
                   usecols=(2),
                   dtype=int
                )

print("avg ", np.mean(array));
print("max ", np.max(array));
print("min", np.min(array));
print("salary hike", array + 1000)
print("total salary", np.sum(array))
print("total hike with 10%", array * 1.10)