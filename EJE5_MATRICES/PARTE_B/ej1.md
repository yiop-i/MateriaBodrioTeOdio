## Matrices con filas dinámicas

Recordemos que la matriz no es nada más que una lista, pero que adentro tiene listas. Entonces, podemos definir la cantidad de filas que tiene una matriz dinámicamente utilizando el comando append.

Si definimos una lista " matriz = [] ", luego podemos añadir filas a la matriz con el comando "append". Si quisiera, por ejemplo, añadir 5 filas a la matriz, puedo hacerlo de la siguiente forma:

'''
for i in range(5):
    matriz.append([])

'''

De esta forma estamos haciendo un append() de listas vacías a la lista original, o lo que es lo mismo, añadiendo filas a la matriz. Terminamos con una lista que adentro tiene 5 listas (una matriz de 5 filas).

Por supuesto que podemos reemplazar el "5" por el valor de una variable de así quererlo.


## Ejercicio 1

### Pedirle al usuario un número de filas y un número de columnas. Luego, hacer que el programa imprima una matriz con tantas filas y columnas como el usuario pidió. El contenido de cada componente debe ser un caracter "X".

Ejemplo: 

Entradas: 6 y 6 

Resultado:

['X','X','X','X','X','X']
['X','X','X','X','X','X']
['X','X','X','X','X','X']
['X','X','X','X','X','X']
['X','X','X','X','X','X']
['X','X','X','X','X','X']

Entradas: 2 y 4

Resultado:

['X','X','X','X']
['X','X','X','X']

