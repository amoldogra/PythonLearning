# IMMUTBALE - NON-CHNAGABLE
# CONTAIN MORE THAN ONE ELEMENT

z =(10)
print(type(z))

t = (10,20,30,40,20)
print(type(t))
l = len(t)
for a in range(l):
    print(a)
for b in t:
    print(b)

#min func.
print(min(t))

#max func.
print(max(t))

#count func.
print(t.count(20))

#index func.
print(t.index(20,2,5))

#sum func.
print(sum(t))               #addition of all elements of tupple