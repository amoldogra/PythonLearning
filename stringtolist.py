# to convert a string into a list of words in string
n = input("Enter the value: ")
l= n.split()
print(l)


# to add multiple strings into a list 
f =[]
m = int(input("Enter the no. of elements to add: "))
for a in range(1,m+1):
    h=input("enter the  value " +str(a)+ ":-" )
    f.append(h)
print(f)    

