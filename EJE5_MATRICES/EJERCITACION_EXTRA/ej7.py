matri=[
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30],
    [31,32,33,34,35,36]
]
par=0
impar=0
for i in range(len(matri)):
    for j in range(len(matri[i])):
        if matri[i][j]%2==0:
            par=par+1
        else:
            impar=impar+1
            
print(f"La cantidad de numeros pares es: {par}\n La cantidad de numeros impares es: {impar}")