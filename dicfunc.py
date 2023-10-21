from distro import name


d ={
    "name":"AMOL",
    "fees":2000,
    "duration":"2months"
}

print(d.get("name"))                                #get func.

for a in d.keys():                                  #key func.
    print(a)
print(d.keys())    

for b in d.values():                                #value func.
    print(b)
print(d.values())    

for c,d in d.items():                                 #item func.
    print(c,d)   

# for deleting any element in dictionary their are 2 methods del func. & pop func., both use keys of dict. to delete value

f =dict(name="python", fees=5000)
print(f)                                             #dict func. - to create dictionary

d.update({"fees":10000})
print(d)

