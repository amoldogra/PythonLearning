# calculator class capable of finding square, cube and square root

class Calculator:

    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The Square is {self.number*self.number}") 
    def cube(self):
        print(f"The cube is {self.number*self.number*self.number}")
    def squareroot(self):
        print(f"The Squareroot is {self.number**1/2 }")       
    @staticmethod
    def hello():
        print("Hello, sohneyo code chlda aa fer ")    

a = Calculator(4)   
a.hello()
a.square()
a.cube()
a.squareroot()

