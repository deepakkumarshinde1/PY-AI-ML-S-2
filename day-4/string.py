text = "my name is Deepakkumar."
# print(text)
# print(text.upper())
# print(text.lower())
# print( len(text) )
# print( text.title() )
# print( text.capitalize() )

text = "    om   "

# print(len(text))
# print(len(text.strip()))

text = "Mango is sweet in taste."
# print(text.startswith('Mam'))
# print(text.endswith('ste.'))

dob = "31-01-2007"
# string ==> array i.e list

print(dob)
print(dob.split('-'))
dob_list = dob.split('-')
# array => string
# _list = ["1","2","3","4","5"]
new_dob = "/".join(dob_list)
print(new_dob)

text = "Omkar is a good boy."
print(text)
print(text.replace("good","bad"))

