w = "Welcome"
print(w.find('e'))
print(w.find('e',3))  # 3 is used to start find from index 3
print(w.index('l'))
print(w.index('e',3))
print(w.isalpha())  # to check all elemets are alphabets
a = "123"
print(a.isdigit())  # to check all elemets are digits
b = "Welcome123"
print(b.isalnum()) # to check variable contain alphabets and number without space & if any special character find in this will give output as FALSE

print(chr(65))   # to convert numeric value to ASCII value
print(ord("A"))   # to convert ASCII value to numeric value
print("Welcome to {} python {}".format("your","tut"))   
print("Welcome to {1} python {0}".format("your","tut"))
print("Welcome to {first} python {second}".format(first = "your",second = "tut"))      

