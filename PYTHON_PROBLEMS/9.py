class  Animal:
    pass    
class Pets(Animal):    
    pass
class Dog(Pets):
    @staticmethod    
    def bark():
        print("Fuck you!!!")

d = Dog()
d.bark()
