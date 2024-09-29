#game using file handiling
#associated file - hiscore.txt



import random


def game():
    print("Youo are playing the game..")
    score = random.randint(1,62)
    # fetch hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if hiscore!="":
            hiscore=int(hiscore)
        else:
            hiscore = 0    
    print(f"Your Score: {score}")
    if score>hiscore or hiscore == "":
        #his hiscore in file
        with open ("hiscore.txt", "w") as f:
            f.write(str(score))


    return score

game()  