matrixoflidership=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
cantcolumna=len(matrixoflidership[0])
for i in range(cantcolumna):
    suma = sum(matrixoflidership[j][i] for j in range(len(matrixoflidership)))
    print(f"Suma de la columna {i}: {suma}")
