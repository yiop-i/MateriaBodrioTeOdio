### 4. Mostrar todos los datos
"""""
Dado el siguiente diccionario:

```python
alumno = {
    "nombre": "Juan",
    "edad": 16,
    "curso": "4°B",
    "promedio": 7.8
}
```

Mostrar cada elemento con el siguiente formato:

```text
nombre: Juan
edad: 16
curso: 4°B
promedio: 7.8
```

> **Pista:** investigar el método `items()`.
"""
alumno = {
    "nombre": "Juan",
    "edad": 16,
    "curso": "4°B",
    "promedio": 7.8
}
for key, value in alumno.items():
    print(key, ":", value)

### 5. Contar elementos
"""""
Crear un diccionario con los votos obtenidos por distintos candidatos:

```python
votos = {
    "Ana": 35,
    "Pedro": 42,
    "Lucía": 28,
    "Martín": 51
}
```

Mostrar la cantidad de candidatos.

Resultado esperado:

```text
Cantidad de candidatos: 4
```

No contar los elementos manualmente.
"""""
votos = {
    "Ana": 35,
    "Pedro": 42,
    "Lucía": 28,
    "Martín": 51
}
print("Cantidad de candidatos:", len(votos))

### 6. Encontrar el mayor
"""""
Utilizando el diccionario del ejercicio anterior, determinar quién obtuvo la mayor cantidad de votos.

Resultado esperado:

```text
Ganador: Martín
Votos: 51
"""
clave, valor = max(votos.items(), key=lambda item: item[1])
print("Ganador:", clave)
print("Votos:", valor)
