import pandas as pd

student_data = {
    "Roll Number": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": [
        "Aarav Sharma",
        "Priya Patil",
        "Rahul Verma",
        "Sneha Joshi",
        "Rohan Kulkarni",
        "Ananya Gupta",
        "Vivek Singh",
        "Neha Desai",
        "Karan Mehta",
        "Pooja Nair"
    ],
    "Age": [18, 19, 20, 18, 21, 19, 20, 18, 22, 19],
    "Marks": [85, 92, 78, 88, 67, 95, 81, 76, 89, 91],
    "City": [
        "Pune",
        "Mumbai",
        "Nashik",
        "Nagpur",
        "Aurangabad",
        "Thane",
        "Kolhapur",
        "Solapur",
        "Satara",
        "Jalgaon"
    ]
}

# Create DataFrame
dfStudent = pd.DataFrame(student_data)

# df.head(n)
# print(dfStudent.head(1))

# df.tail(n)
# print(dfStudent.tail(3))

# df.sample(n)
# print(dfStudent.sample(2))

# df.shape
# print(dfStudent.shape)

# df.size
# print(dfStudent.size)

# df.ndim
# print(dfStudent.ndim)

# df.index
# print(dfStudent.index)

# df.columns
# print(dfStudent.columns)

#df.dtype
# print(dfStudent.dtypes)

# df.values
# print(dfStudent.values)

# df.info
# print(dfStudent.info())

# df.select_dtype
print(dfStudent.select_dtypes(include="object"))

