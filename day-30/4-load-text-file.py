import numpy as np

# dtype is float64 as default
array = np.loadtxt("marks.txt",dtype=int)
# print(array)


array = np.loadtxt("students_marks_2.csv",dtype=int,delimiter=",")
print(array)

array = np.loadtxt("students_marks_2.csv",dtype=int,delimiter=",",usecols=(0,1))
print(array)

array = np.loadtxt("students_marks.csv",dtype=int,delimiter=",",skiprows=1)
print(array)


array = np.loadtxt("students_marks_3.csv",dtype=int,delimiter=",",skiprows=1,usecols=(1,2,3))
print(array)
