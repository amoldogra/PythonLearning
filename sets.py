# UNORDERED & UNINDEXED
# REPETITION OF ELEMENT IS NOT ALLOWED

s = {20,30,40,50,40}
print(s)

#output - {40, 50, 20, 30}

#set func. - to convert any other data type accept dictionary into set
l =[11,22,33,44]
print(set(l))

#add func.
s.add(66)
print(s)   #add func. add element in set on [0] index

#pop func. - delete last element from the set
print(s.pop())
print(s)     

#remove func. 
s.remove(40)
print(s)

#discard func.
s.discard(20)
print(s)

#update func. - to add new list or elements in set and the repetition is clear by set
q = [55,30,66]
s.update(q)
print(s)

#clear func.  - clear function do not give empty curly brackets as output it give output as [Set()] bcoz empty brackets indicates dictionary
s.clear()
print(s)


