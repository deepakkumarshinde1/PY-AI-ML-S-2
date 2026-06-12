# [] => list
# () => tuples
# {} => set
# {key:value} => dictionary

# list
#  1. store data
#  2. list are commonly used to add more than one values, that is the duplication of data.
#  3. List are mutable in nature.

# Tuples
# 1. It can store a data.
# 2. So say the tuples are fixed in nature.That is you will not able to modify that.
# 3. Handles duplicate values.
# can convert a tuples to list.
# We can also convert list to tuples.

number = (1,2,3,4,5,5,5,5,5,5,5,5)
# print(number)


role = ("Student","Admin","Teacher","Finance","Mentor","Staff","Student")

mix = (1,"abc",True)

#print(role[0])
#print(role[2:5]) #indexing 

# role[0] = "Admin"

# method
# print(role.count("Student"))
# print(role.index("Student"))


# tuples to list
roleList = list(role)  # ['Student', 'Admin', 'Teacher', 'Finance', 'Mentor', 'Staff', 'Student']

# list to tuples
roleTuples = tuple(roleList) #('Student', 'Admin', 'Teacher', 'Finance', 'Mentor', 'Staff', 'Student')
# print(roleTuples)

# Concatenation
t1 = (1,2,3,4,5)
t2 = (11,22,33,44)
t3 = t1 + t2
#print(t3)

# Repetition.
t1 = ("deepak",) * 3 #("deepak","deepak","deepak")
# print(t1)
# If a tuple has a single value, kindly add a comma after the end of that value.

# loop
for value in role:
    # print(value)
    pass

# nested tuples
students = (
    ("deepak",37),
    ("om",21),
    ("sakshi",22)
)

# print(students)

# Packing tuples.
a1 = (1,2,3,4)

# Unpacking Tuples
b1,b2,b3,b4 = a1
print(b1,b2,b3)

