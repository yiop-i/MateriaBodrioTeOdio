matriz=[]
fil = int(input("Ingrese la cantidad de filas: "))
col = int(input("Ingrese la cantidad de columnas: "))
for i in range(fil):
    fila = []
    for j in range(col):
        elemento = int(input(f"Ingrese el elemento [{i}][{j}]: "))
        fila.append(elemento)
    matriz.append(fila)
maximo=matriz[0][0]
for i in range(fil):
    for j in range(col):
        if matriz[i][j] > maximo:
            maximo = matriz[i][j]
            fila_max = i
            col_max = j
print("El elemento máximo en la matriz es:", maximo,"en la posición: [", fila_max, "][", col_max, "]")