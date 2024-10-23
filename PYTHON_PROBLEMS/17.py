from functools import reduce

a =[1,2,3,4,5,6,88,99,77,55,22]

def greater(a,b):
    if a>b:
        return a
    return b

print(reduce(greater, a))