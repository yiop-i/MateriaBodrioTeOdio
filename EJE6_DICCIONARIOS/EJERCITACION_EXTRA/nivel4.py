### 9. Contador de palabras
"""
Pedir al usuario que ingrese una frase.

Utilizar un diccionario para contar cuántas veces aparece cada palabra.

Por ejemplo, ante:

```text
python es divertido y python es poderoso
```

El resultado debería ser:

```python
{
    "python": 2,
    "es": 2,
    "divertido": 1,
    "y": 1,
    "poderoso": 1
}
"""
texto = input("Ingrese una frase: ")
palabras = texto.split()
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")
    
### 10. Notas de alumnos
"""
Crear un diccionario donde cada alumno tenga una lista de notas:

```python
alumnos = {
    "Juan": [7, 8, 6],
    "Ana": [9, 10, 8],
    "Pedro": [5, 6, 4]
}
```

Calcular y mostrar el promedio de cada alumno.

Resultado esperado:

```text
Juan: 7.0
Ana: 9.0
Pedro: 5.0
"""
alumnos = {
    "Juan": [7, 8, 6],
    "Ana": [9, 10, 8],
    "Pedro": [5, 6, 4]
}
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio}")

### 11. Diccionarios dentro de diccionarios
"""
Representar información de varios alumnos utilizando diccionarios anidados:

```python
alumnos = {
    "Juan": {
        "edad": 17,
        "curso": "5A",
        "promedio": 8.2
    },
    "Ana": {
        "edad": 16,
        "curso": "5B",
        "promedio": 9.1
    }
}
```

Mostrar la siguiente información:

```text
Juan estudia en 5A y tiene promedio 8.2
Ana estudia en 5B y tiene promedio 9.1
"""
alumnos = {
    "Juan": {
        "edad": 17,
        "curso": "5A",
        "promedio": 8.2
    },
    "Ana": {
        "edad": 16,
        "curso": "5B",
        "promedio": 9.1
    }
}
for nombre, info in alumnos.items():
    print(f"{nombre} estudia en {info['curso']} y tiene promedio {info['promedio']}")