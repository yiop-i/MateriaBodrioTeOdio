# Ejercicio de temperaturas de una ciudad.

El gobierno de Vice City ha decidido instalar tótems que toman la temperatura en distintos puntos de la ciudad. En total ha instalado 9 tótems en las calles, que corresponden a la siguiente distribución:

NOROESTE, NORTE, NORESTE
OESTE, CENTRO, ESTE
SUROESTE, SUR, SURESTE

El alcalde de la ciudad le ha pedido que realice un programa que:

1. Muestre un menú interactivo con las opciones:
    - Ver temperatura promedio
    - Ver temperatura puntual
    - Ver temperatura franja superior
    - Ver temperatura franja central
    - Ver temperatura franja sur

2. Si elige la primer opción, mostrará la temperatura promedio de toda la ciudad.
3. Si elige la segunda opción, pedirá que ingrese uno de los totems específicos (NORTE, ESTE, OESTE, SUR, NOROESTE, NORESTE, etc...) y imprimirá cuál es la temperatura tomada por dicho tótem.
4. Si elige una de las últimas tres opciones, imprimirá el promedio de las 3 temperaturas correspondientes a la fila que corresponda. 

Notas:

La matriz que tiene que generar será una con números aleatorios flotantes entre 20 y 23. Para generar cada número aleatorio puede usar el siguiente comando

'''
random.uniform(20, 23)
'''

También debe estar redondeado a un solo decimal, para lo que puede utilizar el comando

'''
round(numero, 1)
'''

O si lo prefiere, puede combinar los comandos de la siguiente forma:

'''
num_aleatorio = round(random.uniform(20,23), 1)
'''

También, en esta consigna se entiende como "tótem" a un aparato con forma cilíndrica que se pone en la calle que mide la temperatura y la muestra en una pantalla.

DEBE USAR MATRICES.