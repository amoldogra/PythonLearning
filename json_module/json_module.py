import json
#jsom module/inbuilt-library is used to convert json format file into python dictionary

j ='[{"cname":"python","fees":"none","duration":"lifetime"}]'

x = json.loads(j)
print(x)


#read json file
file = open("grades.json","r")
z = file.read()
a = json.loads(z)
print(a)

for l in a:
    print(a)
    print(a["score"])

    

