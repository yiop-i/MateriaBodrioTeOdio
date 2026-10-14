# Introducción a diccionarios

El diccionario es una estructura de datos que está definida con llaves y almacena _varios elementos_ en pares _clave, valor_.
Esto significa que podemos tener muchos valores en un solo diccionario, y cada uno de esos valores tendrá una clave única dentro del diccionario.

Las claves y valores pueden estar conformadas por el tipo de dato que se desee, pero todas las claves y todos los valores deben pertenecer al mismo tipo de datos para tener consistencia.

Un ejemplo de diccionario es el siguiente:


```personas = {
    126: "Juancito",
    233: "Pepito",
    333: "María",
    453: "Estela"
}
```


En donde tenemos una serie de claves [126, 233, 333, 453] de tipo entero (int) y una serie de valores ["Juancito", "Pepito", "María", "Estela"] de tipo cadena de caracteres / string (str).

Para acceder al valor de un diccionario, debemos invocar el nombre de la variable en la que está definido el diccionario y luego, entre corchetes, pasarle la clave. De esta forma, se nos devolverá el valor que corresponde a la clave que ingresamos.

```
print(peronas[126]) ← Esto imprimirá "Juancito", porque ese es el valor que corresponde a la clave 126.
```

Si queremos iterar en los valores de un diccionario, tenemos dos formas:

Iterar por los VALORES
Iterar por las CLAVES

Si quiero tener acceso tanto a claves como valores, itero por las claves, ya que una clave me da acceso directo al valor. Ejemplo: Si la clave actual en una iteración se guarda en una variable _key_, la primera iteración _key_ será igual a 126, y al hacer personas[key] va a ser lo mismo que hacer personas[126], y esto es el valor "Juancito". 
Si no me interesa tener acceso a las claves y quiero simplemente ver los valores, itero por los valores. Si tengo solo los valores no puedo tener acceso a las claves.

Cada diccionario tiene un método _keys()_ y un método _values()_ que devuelven las claves y valores respectivamente, en el formato de una lista / objeto iterable. 

personas.keys() devuelve [126, 233, 333, 453]
personas.values() devuelve ["Juancito", "Pepito", "María", "Estela"]

Para iterar en las llaves entonces se hace:
```for key in personas.keys():
    ...
```

Para iterar en los valores se hace:
```for value in personas.values():
    ...
```

El ejercicio actual es sacarse todas las dudas que genere este marco teórico con el profesor o una inteligencia artificial predilecta.