class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def displayBikes(self):
        print("Total bikes:-",self.stock)
    def rentForBike(self,r):

        if r<0:
            print("Enter the +ve value and greater than zero")
        elif r>self.stock:
            print("Enter the value less than stock")
        else:
            print("Total price:-",r*100)
            self.stock = self.stock-r
            print("Total Bikes remaining:-",self.stock)

while True:
    obj = BikeShop(100)
    uc = int(input(''' 
1 Display Stocks
2 Rent a Bike
3 Exit                                      '''))    
    
    if uc==1:
        obj.displayBikes()
    elif uc==2:
        n = int(input("No. of Bike(s) needed"))
        obj.rentForBike(n)  
    else:
        break    





