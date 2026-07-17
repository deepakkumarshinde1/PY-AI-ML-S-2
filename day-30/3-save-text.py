import numpy as np

marks = np.array([10,30,50,20,5])

np.savetxt("marks.txt",marks,fmt="%d")

# fmt => output format
# %.18e (default) (Scientific notation)
# %d => int
# %.2f => decimal with 2 val
# %.3f => decimal with 3 val
# %s => string

marks = np.array([
    ["Name","Maths","Science","English"],
    ["Deepak",10,20,30],
    ["Raj",40,50,60],
    ["Archana",70,80,90]
])
marks = np.array([
    ["Maths","Science","English"],
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

np.savetxt("students_marks.txt",marks,fmt="%s",delimiter="\t")
np.savetxt("students_marks.csv",marks,fmt="%s",delimiter=",")
np.savetxt("s_marks.csv",marks,fmt="%s",delimiter=",")