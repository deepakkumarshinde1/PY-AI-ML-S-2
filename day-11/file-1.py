# file handling 
# text file => .txt .cvs .json
# binary file => .png .jpg .mp3 .mp4 .exe .pdf => 101010

# file handling mode
# r => read file
# w => write file
# a => append file
# x => create file if not exists
# r+ => read & write
# w+ => write & read
# br => binary read
# bw => binary write

# read
#file = open('student.txt','r')
#print(file.read())
# if file don't exists you will get error

# write
#ile = open('payment.txt','w')
#file.write('Shinde Deepakkumar')
#  if file don't exists it will create a new file

# appending
file = open("students.txt",'a')
file.write('\n Om Jadhav')
# if file don't exists it will create a new file
