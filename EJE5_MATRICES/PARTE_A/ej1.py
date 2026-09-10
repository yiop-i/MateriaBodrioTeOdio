# Genera una matriz 5x5 y permite marcar posiciones con una "X"
matriz = [[0 for _ in range(5)] for _ in range(5)]

while True:
    try:
        fila = int(input("Ingrese la fila (1-5): "))
        columna = int(input("Ingrese la columna (1-5): "))
    except ValueError:
        print("Debe ingresar números enteros.")
        continue

    if not (1 <= fila <= 5 and 1 <= columna <= 5):
        print("La fila y la columna deben estar entre 1 y 5.")
        continue

    # Ajustamos para usar índices de Python (0 a 4)
    fila -= 1
    columna -= 1

    # Colocamos la X en la posición elegida
    matriz[fila][columna] = "X"

    # Mostramos la matriz actualizada
    for fila_matriz in matriz:
        print(" ".join(str(valor) for valor in fila_matriz))

    print("\n" + "-" * 20 + "\n")
