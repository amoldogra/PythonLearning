
try:
    with  open("1.txt","r") as a:
        print(a.read()) 
except Exception as e:
    print(e)

try:        
    with  open("2.txt","r") as b:
          print(b.read()) 
except Exception as e:
    print(e)


try:        
    with  open("3.txt","r") as c :
          print(c.read()) 
except Exception as e:
    print(e)



