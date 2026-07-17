#  School stores Marks of a student's In different subject.
# A principal wants to quickly analysis. Data to find out.
# 1 Average marks.
# 2. Highest marks
# 3. Lowest marks
# 4. Understand the data set of given data.
import numpy as np
studentDataset = np.array([
    # Math Geography English
    [80, 90, 85], # amit
    [70, 95, 88], # soham
    [60, 75, 92], #arun
    [95,98,99] #suraj
    
])

print("average marks ", np.mean(studentDataset))
print("Highest marks  ", np.max(studentDataset))
print("Lowest  marks  ", np.min(studentDataset))

# Understand the data set
print("dim ", studentDataset.ndim)
print("shape ", studentDataset.shape)
print("size ", studentDataset.size)


