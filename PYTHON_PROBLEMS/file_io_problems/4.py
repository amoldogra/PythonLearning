# replace donkey word with ### from file donkey4.txt 


word = "Donkey"

with open("donkey4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "####")
with open("donkey4.txt", "w") as f:
    f.write(contentNew)


#  if we need to replace multiple word with single word 
# words = ["Donkey","Monkey","Ponkey"]

# with open("donkey4.txt", "r") as f:
#     content = f.read()
# for word in word:
#      content = content.replace(word, "#" *len(word))
# with open("donkey4.txt", "w") as f:
#     f.write(content)