# we need to from a to b but 
# list must be only of even insert number

n1 = int(input("Enter 1st number = "))
n2 = int(input("Enter 2st number = "))
_list = []
for value in range(n1,n2+1):
    if value % 2 == 0:
        _list.append(value)

print(_list)