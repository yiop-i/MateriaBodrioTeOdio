# Ejercicios de Python — Diccionarios

## 🟢 Nivel 1 — Acceso y modificación

### 1. Información de una persona

Crear un diccionario que represente a una persona:

```python
persona = {
    "nombre": "Ana",
    "edad": 17,
    "curso": "5°A",
    "promedio": 8.5
}
```

Mostrar por pantalla:

- Nombre
- Edad
- Curso
- Promedio

---

### 2. Modificar valores

Partiendo del diccionario del ejercicio anterior:

1. Cambiar la edad a `18`.
2. Cambiar el promedio a `9`.
3. Agregar una clave `"ciudad"` con el valor `"Mendoza"`.
4. Mostrar el diccionario completo.

---

### 3. Consultar una clave

Crear un diccionario que represente un producto:

```python
producto = {
    "nombre": "Teclado",
    "precio": 25000,
    "stock": 15
}
```

Pedir al usuario una clave y mostrar su valor.

Ejemplo:

```text
¿Qué dato querés consultar? precio
25000
```

---

## 🟡 Nivel 2 — Recorrer diccionarios

### 4. Mostrar todos los datos

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

---

### 5. Contar elementos

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

---

### 6. Encontrar el mayor

Utilizando el diccionario del ejercicio anterior, determinar quién obtuvo la mayor cantidad de votos.

Resultado esperado:

```text
Ganador: Martín
Votos: 51
```

---

## 🟠 Nivel 3 — Diccionarios + entrada de datos

### 7. Agenda telefónica

Crear un programa que permita administrar una agenda telefónica.

El programa debe mostrar un menú:

```text
1. Agregar contacto
2. Buscar contacto
3. Mostrar contactos
4. Salir
```

Los contactos deben almacenarse en un diccionario:

```python
agenda = {
    "Juan": "2615551234",
    "Ana": "2614445678"
}
```

Al agregar un contacto, el usuario debe ingresar:

- Nombre
- Número de teléfono

Al buscar un contacto, el programa debe mostrar su número.

---

### 8. Inventario

Crear un programa que administre el stock de una tienda.

Utilizar inicialmente:

```python
inventario = {
    "mouse": 15,
    "teclado": 8,
    "monitor": 4,
    "auriculares": 12
}
```

El programa debe permitir:

- Consultar el stock de un producto.
- Agregar unidades a un producto.
- Quitar unidades de un producto.
- Agregar un producto nuevo.
- Mostrar todo el inventario.

Ejemplo:

```text
Producto: mouse
Stock actual: 15

¿Cuántas unidades querés agregar? 5

Nuevo stock: 20
```

---

## 🔴 Nivel 4 — Procesamiento de información

### 9. Contador de palabras

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
```

---

### 10. Notas de alumnos

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
```

---

### 11. Diccionarios dentro de diccionarios

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
```

---

## 🔥 Desafío final — JSON y diccionarios

### 12. Procesar datos de una API

Crear un archivo llamado `alumnos.json` con el siguiente contenido:

```json
{
    "alumnos": [
        {
            "nombre": "Juan",
            "edad": 17,
            "curso": "5A",
            "promedio": 8.2
        },
        {
            "nombre": "Ana",
            "edad": 16,
            "curso": "5B",
            "promedio": 9.1
        },
        {
            "nombre": "Pedro",
            "edad": 17,
            "curso": "5A",
            "promedio": 6.7
        }
    ]
}
```

Crear un programa Python que:

1. Abra el archivo `alumnos.json`.
2. Utilice el módulo `json` para cargar los datos.
3. Muestre los nombres de todos los alumnos.
4. Muestre solamente los alumnos cuyo promedio sea mayor o igual a `8`.
5. Calcule y muestre el promedio general de todos los alumnos.
6. Pida al usuario el nombre de un alumno y muestre toda su información.
7. Si el alumno no existe, mostrar un mensaje indicando que no fue encontrado.

### Ejemplo

```text
Alumnos:
- Juan
- Ana
- Pedro

Alumnos con promedio >= 8:
- Juan: 8.2
- Ana: 9.1

Promedio general: 8.0

Ingrese un alumno: Ana

Información:
Edad: 16
Curso: 5B
Promedio: 9.1
```

> **Objetivo:** comprender que los datos recibidos desde archivos JSON y APIs se representan naturalmente mediante **diccionarios, listas y combinaciones de ambos** en Python.
