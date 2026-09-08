# Ejercicio de puntajes

El señor Guido Kaczka, conductor de un novedoso programa de televisión, se le acercó para pedirle que programe una solución informática para uno de sus juegos para que la producción pueda llevar un conteo de los jugadores y los puntajes. 

Las reglas del juego son las siguientes:
Son 9 los jugadores.
Los mismos están dispuestos a modo de grilla, distribuidos en filas de 3 personas.
Cuando se juega una ronda, Guido les hace preguntas a los jugadores en forma secuencial, empezando de arriba a la izquierda y siguiendo hacia la derecha y, terminada la fila, hacia abajo.
Si la persona responde la pregunta de forma correcta, sigue jugando. Si la persona responda la pregunta de forma incorrecta, pierde 10 puntos.
Además, se van a eliminar todos los jugadores que tengan puntos negativos una vez sea terminada una ronda.
También existe un bonus que pueden ganar los jugadores en el que se toman a todos los espacios de jugadores disponibles y se elije aleatoriamente un lugar para eliminar.


El programa debe mostrar indefinidamente un menú como el siguiente:

['', '', '']
['', '', '']
['', '', '']

1. Cargar jugadores
2. Jugar ronda
3. Eliminación
4. Eliminación aleatoria
5. Salir

- Si se elije "Cargar jugadores", se pedirán los nombres de los nueve jugadores uno a uno. Cuando vuelva a aparecer el menú, los nombres de los jugadores deben estar cargados en la matriz sobre el menú.
- En OTRA MATRIZ paralelamente, deben irse cargando los puntajes de los jugadores. Al principio cada uno tiene un puntaje de 10 por defecto.
- Cada vez que se selecciona "Jugar ronda", se le pide a la persona que está utilizando el programa que ingrese "V" si el jugador respondió correctamente a la pregunta y "F" si la respondió incorrectamente. Si se registra una respuesta como "F", se le quitarán 10 puntos al jugador que corresponda. Esto es para cada uno de los 9 jugadores; osea que tiene que preguntar 9 veces si se respondió correctamente a la pregunta, siempre que jueguen los 9. Si ya se eliminó algún jugador, no se preguntará si respondió bien o mal.
- Si se selecciona "Eliminación", los nombres de los jugadores que tienen puntaje negativo son eliminados. 
- Si se selecciona "Eliminación aleatoria", se seleccionará un espacio aleatorio (fila aleatoria entre 0 y 2 y columna aleatoria entre 0 y 2). Si hay un nombre en esa casilla, el jugador que toque será eliminado.
- Si se aprieta el botón "Salir", el programa debe cerrarse.

Notas:

Tomense su tiempo en entender de qué trata el problema porque es complejo.

Hagan dos matrices por separado: Una de participantes (que lleva los nombres y debe ser mostrada cada vez que carga el menú con aquellos participantes que sigan en pie) y otra de puntajes (en donde cada número que vaya en cada lugar corresponda al participante que lleva el mismo lugar en la matriz de participantes).
