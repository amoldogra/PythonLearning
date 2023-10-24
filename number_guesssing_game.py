import random
m = int(input("ENTER NUMBER B/W 1-100 :-"))
if m >100 or m <1:
    print("INVALID INPUT")
else:    
   print("COMPUTER VALUE :-")
   n = random.randint(1,100)
   print(n)
   if (m > n):
       print("YOUR VALUE IS LARGER THAN COMPUTER")    
   elif m ==n:
       print("YOUR VALUE IS EQUAL TO COMPUTER")    
   else:
       print("YOUR VALUE IS LESSER THAN COMPUTER")

