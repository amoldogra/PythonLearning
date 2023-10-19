l =[33,222,33,44,55,66]
print(l.count(33))              #count func. - to count repetition of any element in list

print(max(l))                   #max func.  - maximum value in list

print(min(l))                   #min func. - minimum value in list

l.sort()                        #sort func.
print(l)

l.reverse()                     #reverse func.
print(l)                      

g =[22,33,44,33,55,77]
print(g.index(33,2,4))          #index func.  - syn - index(elemrnt, start_index, end_index) -  if element is repeated in list
print(g.index(33))