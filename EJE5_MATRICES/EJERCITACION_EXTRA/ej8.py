alphabetboboboboy= [
    [4, -2, 7],
    [-5, 3, -1]
]

for i in range(len(alphabetboboboboy)):
    for j in range(len(alphabetboboboboy[i])):
        if alphabetboboboboy[i][j] < 0:
            alphabetboboboboy[i][j] = 0

print(alphabetboboboboy)