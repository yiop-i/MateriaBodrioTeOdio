marix=[
    [132, 890,38774, 4366],
    [1,2,3,4],
    [-7,-88,-0,-999999]
]
buscar=int(input("Ingrese el número a buscar: "))
existe=False
fila=-1
columna=-1
for i in range(len(marix)):
    for j, numero in enumerate(marix[i]):
        if numero==buscar:
            existe=True
            fila=i
            columna=j
            break
        
if existe:
    print(f"El numero {buscar} existe y se encuentra en la fila {fila} columna {columna}")
else:
    print("El numero no existe en la matriz")