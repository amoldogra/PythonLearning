# the perfect guess

import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a!=n):
    guesses+=1
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses+=1
    elif(a<n):
        print("HIgher number Please") 
        guesses+=1
print(f"Yoou hav guessed the number correctly in {guesses} attempts")           