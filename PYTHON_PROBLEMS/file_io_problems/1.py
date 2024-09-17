#file i/o problems
# read text from given file and check whether it contains desired word in i


f = open("poem.txt")
data = f.read()
if "twinkle" in data:
    print("Twinkle is present")
else:
    print("Not FOund")    
f.close()


