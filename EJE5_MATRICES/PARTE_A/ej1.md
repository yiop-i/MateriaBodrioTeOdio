## ¿Qué es una matriz?

La matriz es una estructura de datos que actúa, en escencia, como una lista de listas.

Si una lista _lista1_ tiene los elementos "A", "B", "C", una matriz _matriz1_ tiene como elementos *listas*. 

lista1 = ["A", "B", "C"]

matriz1= [
    ["A", "B"]
    ["C", "D"]
]

Hay que prestarle atención a la forma que tiene esta estructura de datos. Cuando hablábamos de listas, estabamos viendo
una estructura de datos que tenía elementos dentro. 

lista1[2] # Acá podemos ver cómo estamos accediendo al elemento del lugar *2* de nuestra lista. Si contamos desde el 0, podemos
          # ver que dicho elemento es una letra "C".
lugar:            0   1   2   
elemento:        [A] [B] [C]
                          ↑

lista1[0] # En este caso, tomaría el lugar 0 de la lista, osea, "A".
lugar:            0   1   2   
elemento:        [A] [B] [C]
                  ↑


Las matrices funcionan de la misma forma, solo que en vez de un caractér o número, en cada uno de los lugares de esta "lista de listas"
tendremos acceso a una lista.
matriz1[0] # Esto imprime una lista entera, la que corresponde a la primer fila.
matriz1[1] # Esto imprime una lista entera, la que corresponde a la segunda fila.

lugar:                 0           1      
elemento:        [["A", "B"]] [["C", "D"]]

Lo que está en el lugar 0 es ["A", "B"], osea una lista entera. Lo mismo con la fila que está guardada en el lugar 1.

Podemos acceder a un elemento particular mencionando a qué fila queremos hacer referencia y a qué columna. Hay que pensarlo
de la siguiente forma:
    C0    C1
F0 ["A", "B"]
F1 ["C", "D"]

Donde F significa FILA y C significa COLUMNA. 
Para acceder a un elemento, especificamos a qué FILA y a qué COLUMNA pertenece de la siguiente forma

matriz1[0][0] # Imprime "A"
matriz1[0][1] # Imprime "B"
matriz1[1][0] # Imprime "C"
matriz1[1][1] # Imprime "D"

## Consigna

### Generar un archivo "ej1.py" en el presente directorio. Copiar y pegar en el chat de la inteligencia artificial lo siguiente:

*Quiero que crees un programa en Python que genere una matriz de cinco filas y cinco columnas, y luego le pida al usuario infinitamente
que ingrese coordenadas (fila y columna). Luego, quiero que aparezca una "X" en la fila y columna que eligió el usuario. Una vez termines,
dame el código y explícame tu razonamiento.*

### Luego, responder las preguntas manualmente y a consciencia, intentando no utilizar IA, en un archivo respuestas1.md en este mismo directorio:

1. ¿Qué es una matriz?
2. ¿Cómo se organizan las matrices?
3. ¿Cómo puedo acceder a una fila entera de una matriz?
4. ¿Cómo puedo acceder a un elemento de una matriz?
5. Desarrolle verbalmente cómo implementó la Inteligencia Artificial la solución pedida. 
