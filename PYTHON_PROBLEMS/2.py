#Handling missing keys in Python dictionaries

dict = {"name":1, "age":23, "c":3}
if "d" in dict.keys():
    print(dict["d"])
else:
    print("Item not found")    