# Get size of a Dictionary in Python

import sys
# use SYS  module to get size of python list, dictionary , tupple and for a single varibale

dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
lst = [1,2,33,4]

print("Size od dic1: " + str(sys.getsizeof(dic1))+ " bytes")
print("Size od dic2: " + str(sys.getsizeof(dic2))+ " bytes")
print("Size od dic3: " + str(sys.getsizeof(dic3))+ " bytes")
print(str(sys.getsizeof(lst))+ " bytes")