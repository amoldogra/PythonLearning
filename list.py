# iteration of list elements
l = [5,6,7,8,9,2]
le = len(l)
for n in range(le):        
    print(l[n])

print()    # for spacing b/w output
    # alternative 
for a in l:
    print (a)
   
print()      
 # iteration of list elements in reverse

l = [5,6,7,8,9,2]
le = len(l)
for n in range(le-1,-1,-1):       
    print(l[n])

# ------------------------------------------------------------------------
print()
# ------------------------------------------------------------------------

# list comprehension

l =[]
# create list using APPEND func.
for a in range(1,101):
    l.append(a)              
print (l)

# create list using list comprehension func.

n = [m for m in range(1,101) ]
print(n)

s = "Welcome"
f =[h for h in s]
print(f)

# create list using list comprehension func. with a condition 
n = [m for m in range(1,101) if m%2==0]
print(n)




