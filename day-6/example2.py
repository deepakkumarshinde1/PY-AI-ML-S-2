_list = []
while True:
    number = int(input("Enter number = "))
    _list.append(number)
    char = input("To continue press y else press any key to get sum")
    if char != "y":
        break
sum = 0
for value in _list:
    sum += value

print(f"the sum of given number is = {sum}")