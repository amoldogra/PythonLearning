import pickle

# pickle module - used to read and write data in file (STORE DATA IN SERIALIZED FORM)

#dump func. - to write file.(FOR SERIALISE)
a ={"name":"Amol",
    "age":2,
    "last name" :"Dogra"
    }
b = open("demo.txt","wb")
pickle.dump(a,b)
b.close()

#load func.- to read file. (FOR DE-SERIALZING)
f = open("demo.txt","rb")
l = pickle.load(f)
print(l)