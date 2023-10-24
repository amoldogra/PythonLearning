import random
 
 #randint func. - gives random int. between given range
print(random.randint(5,10))

#randrange func.- gives random number between given range but the endrange value not included
print(random.randrange(5,10))

#choice func.- return random element from list
l =["banana", "apple", "orange"]
print(random.choice(l))

#random fuction - gives any float number b/w 0-1
print(random.random())

#shuffle func. -  shuffle elements of list
random.shuffle(l)
print(l)

# uniform func. - gives any float value b/w given range
print(random.uniform(5,10))