import random
m = input('''ENTER YOUR DECISION ["ROCK", "PAPER", "SCISSOR"]''')

l = ["ROCK", "PAPER", "SCISSOR"]
n = random.choice(l)
print("COMPUTER :-")
print(n)

if m == "PAPER" or m == "paper" and n == "ROCK":
    print("YOU WIN")
elif m=="ROCK" or m =="rock" and n == "PAPER":
    print("YOU LOSE")
elif m =="SCISSOR" or m=="scissor" and n=="SCISSOR  "  :
    print("DRAW")    
elif n=="ROCK" and m =="paper" or m == "PAPER":
    print("YOU WIN")
elif n =="ROCK" and m=="rock" or m=="ROCK"  :
    print("DRAW")     
elif n=="PAPER" and m =="ROCK" or m == "rock":
    print("YOU LOSE")     
elif n=="ROCK" and m =="paper" or m == "PAPER":
    print("YOU WIN")
elif n =="PAPER" and m=="PAPER" or m=="paper"  :
    print("DRAW")     
elif n=="PAPER" and m =="ROCK" or m == "rock":
    print("YOU LOSE")   
elif m=="ROCK" or m =="rock" and n == "SCISSOR":
    print("YOU WIN")
elif m =="PAPER" or m=="paper" and n=="SCISSOR  "  :
    print("YOU LOSE")
elif m=="SCISSOR" or m =="scissor" and n == "PAPER":
    print("YOU WIN")
elif m =="SCISSOR" or m=="scissor" and n=="ROCK  "  :
    print("YOU LOSE")    
else:
    print("INVALID")            
