matriz= [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14]
]

multiplicador=int(input("Ingrese el número por el cual desea multiplicar la matriz: "))
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j]=matriz[i][j]*multiplicador

print(matriz)