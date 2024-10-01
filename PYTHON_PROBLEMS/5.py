
#constructor


class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("gandu", 10000000, 122242)      
print(p.name, p.salary, p.pin)
