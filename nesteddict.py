course = {
    "php":{"ducration":"3 MOnths","fees":15000},
    "java":{"ducration":"2 MOnths","fees":10000},
    "python":{"ducration":"3 MOnths","fees":12000}
}

print(course)
print(course["php"]["fees"])

for a,v in course.items():
    print(a,v)