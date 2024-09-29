# replace donkey word with ### from file donkey4.txt 


word = "Donkey"

with open("donkey4.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "####")
with open("donkey4.txt", "w") as f:
    f.write(contentNew)