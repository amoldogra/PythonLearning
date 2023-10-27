a= input("enter the number")
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {i*int(a)}" )
except:
    print("invalid input")


print("code executed")            


#try and except iused to handle if the logical is correct then execute try and if any logical error occured them code is not giving any error in terminal and run except block      

#for handling specific type of error

try:
    num = int(input("Enter a integer:-"))
    a =[6,7]
    print(a[num])
except ValueError:              #to handle value related error
    print("Number entered is not an integere")
except IndexError:              #to handle index related error
    print("Index Error")        