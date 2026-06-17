
file = open("student.log","w")
file.close()

# File statement
text = input("Enter your name = ")
with open("student.log","a") as file:
    file.write(f"\nname is = {text}")

with open("student.log","r") as file:
    file.seek(4)
    print(file.read(8))
    print(file.tell())