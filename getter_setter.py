class Student:
    def __init__(self):
        self.__name=""       #__variable_name -> "__" shows the variable is private
    def getName(self):       #GETTER
        return self.__name
    def setName(self,a):     #SETTER
        self.__name = a

obj = Student()
obj.setName("Shanty")
print(obj.getName())  
     
#getter and setter used in encapsulation for using it.

