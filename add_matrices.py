num1 = [[1,2,3],
        [3,2,0],
        [4,5,2]]
num2 = [[4,5,2],
        [3,2,0],
        [1,2,3]]
fin = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(num1)):
    for j in range(len(num1[0])):
        fin[i][j] = num1[i][j] + num2[i][j]

print(fin)
for z in  fin:
    print(z)       