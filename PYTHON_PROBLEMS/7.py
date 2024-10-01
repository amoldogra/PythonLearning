#train ticket , status and fare check code


from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"ticket is biooked in train no :{self.trainNo} from {fro} to {to}")

    def status(self):
        
        print(f"Train no: {self.trainNo} is running on time")

    def pinfo(self, fro, to):
        print(f"Ticket fare in train no : {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

p = Train(12345)
p.status()
p.pinfo("columbia", "hollywood")
p.book("columbus", "alberta")