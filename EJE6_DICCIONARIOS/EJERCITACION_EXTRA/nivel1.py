### 1. Información de una persona
"""
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
"""
persona = {
    "nombre": "Ana",
    "edad": 17,
    "curso": "5°A",
    "promedio": 8.5
}
for key, value in persona.items():
    print(key,":", value)
    
### 2. Modificar valores
""""
Partiendo del diccionario del ejercicio anterior:

1. Cambiar la edad a `18`.
2. Cambiar el promedio a `9`.
3. Agregar una clave `"ciudad"` con el valor `"Mendoza"`.
4. Mostrar el diccionario completo.

---
"""
persona["edad"] = 18
persona["promedio"] = 9
persona.update({"ciudad": "Mendoza"})
for key, value in persona.items():
    print(key,":", value)
    
### 3. Consultar una clave
"""""
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
"""
producto = {
    "nombre": "Teclado",
    "precio": 25000,
    "stock": 15
}
clave = input("¿Qué dato querés consultar? ")
print(producto[clave])
