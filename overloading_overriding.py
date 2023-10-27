#overloading -> one function doing more than one execution with different outputs
class A:
    def greeting(self,name=""):
        print("Welcome to my github repository "+name)
obj = A()     
obj.greeting()
obj.greeting("Amol Dogra")   


# EXAMPLE
class Area:
    def findArea(seld,x=None,y=None):
        if x!=None and y!=None:
            print(x*y)
        elif x!=None:
            print(x*x)
        else:
            print("NOTHIG TO PRINT")         

obj1 = Area()
obj1.findArea(10)
obj1.findArea(10,10)
obj1.findArea()


#overriding -> different class with same name and differnt variable and different output 

class Add:
    def output(self,a,b):
        print(a+b)
class Name(Add):        
    def output(self):
       
        print("Welcome to github repository")
        super().output(10,20)  #super func. used to diaplay parent class methods

create = Name()
create.output()

#EXAMPLE 1

class X:
    def showData(self):
        print("in class A")
class Y(X):
    def shoeData(self):
        print("in class B") 
        super().showData()
obj3 =  Y()
obj3.shoeData()              

#EXAMPLE 2

class Square:
    def area(self,side):
        print(side*side)
class Rectangle():
    def area(self, l,h):
        print(l*h)

obj4 = Rectangle()
obj5 = Square()
obj5.area(10)
obj4.area(10,2)                