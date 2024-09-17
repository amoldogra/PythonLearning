#  Sort Python Dictionaries by Key or Value

myDict = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
my_keys = list(myDict.keys())
my_keys.sort()
sorted_dict = {i:myDict[i] for i in my_keys }
print(sorted_dict)

