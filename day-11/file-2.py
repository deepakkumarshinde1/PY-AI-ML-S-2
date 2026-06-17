file = open('my-task.txt','r')

# print(file.read(1))
# print(file.readline())
# print(file.readline())
# print(file.readline())

data = file.readlines() # [line1, line2, line3, line4]
print(data)
file.close()


with open('my-task.txt','r') as file:
    print(file.read())

# auto close
with open('my-task.txt','w') as file1:
    file1.write("\nstatement-1")
    file1.write("\nstatement-1")
    file1.write("\nstatement-1")
    file1.write("\nstatement-1")
    file1.write("\nstatement-1")