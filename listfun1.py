l = [20,30,40,50]
del l[1]                            #delete func.
print(l)

n = [20,30,40,50]
n.pop(2)                            #pop func.
print(l)

#difference b/w pop and del is when we print pop func. it will give output as element which he poped from list but del fucntion is not pritable and if added in print statement it will give an error
print(n.pop(2))

f = [20,30,40,50,60]
f.remove(30)                        #remove func,
print(f)


n.clear()
l.clear()                           #clear func. - remove all elements
print(n,l)

f[2] = 80                           #update func.
print(f)                            

f.append("hello")                   #append func. - to add any element in list    
print(f)
z = [77,44]                         
f.append(z)                     
print(f)

f.insert(1,90)                      #insert func. - insert value at any index -syn- insert(indexvalue, elemrnt)
print(f)

f.extend(z)
print(f)                           #enxtend func. - adding value in list as value of same list 