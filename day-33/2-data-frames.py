import pandas as pd
import numpy as np

# dataFrame

# with list
students = [
    ["Kiran",40],
    ["Vedika",50],
    ["Saish",33],
    ["Bhakti",77]
]
# dfStudent = pd.DataFrame(
#                       students,
#                       columns=["Name","Marks"]
#                       )
# dictionary
students = {
    "Name":["Kiran","Vedika","Saish","Bhakti"],
    "Marks":[400,500,330,770]
}






# list of dictionary
students = [
    {"Name":"Kiran","Fees":40000},
    {"Name":"Vedika","Fees":50000},
    {"Name":"Saish","Fees":33000},
    {"Name":"Bhakti","Fees":77000}
]

data = np.array([
    [10,20],
    [30,40],
    [50,60]
])
dfStudent = pd.DataFrame(
     data,
     columns=["marks","percentage"],
     index=["A","B","C"]
    )
print(dfStudent)