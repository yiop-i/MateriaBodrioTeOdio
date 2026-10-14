## 🟠 Nivel 3 — Diccionarios + entrada de datos

### 7. Agenda telefónica
"""""
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
"""
agenda = {
    "Juan": "2615551234",
    "Ana": "2614445678"
}
programa = True
opciones = ["1. Agregar contacto", "2. Buscar contacto", "3. Mostrar contactos", "4. Salir"]
print("Bienvenido a la agenda telefónica")
while programa:
    for opcion in opciones:
        print(opcion)
    eleccion = input("Ingrese una opción: ")
    if eleccion == "1":
        nombre = input("Ingrese el nombre completo del contacto: ")
        telefono = input("Ingrese el número de teléfono: ")
        agenda.update({nombre: telefono})
        print(f"El contacto {nombre} ha sido agregado correctamente")
    elif eleccion == "2":   
        valor_buscado = input("Ingrese el nombre del contacto que desea buscar: ")
        for key, value in agenda.items():
            if key == valor_buscado:
                print(f"El número de teléfono de {key} es: {value}")
                break
        else:
            print(f"El contacto {valor_buscado} no se encuentra en la agenda")
    elif eleccion == "3":
        print("Contactos en la agenda:")
        for key, value in agenda.items():
            print(f"{key}: {value}")
    elif eleccion == "4":
        print("Saliendo del programa...")
        programa = False

### 8. Inventario
"""""
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
"""
inventario = {
    "mouse": 15,
    "teclado": 8,
    "monitor": 4,
    "auriculares": 12
}
posibilidades = ["1. Consultar stock", "2. Agregar unidades", "3. Quitar unidades", "4. Agregar producto nuevo", "5. Mostrar inventario", "6. Salir"]
programa = True
while programa:
    for opcion in posibilidades:
        print(opcion)
    eleccion = input("Ingrese una opción: ")
    if eleccion == "1":
        producto = input("Ingrese el nombre del producto que desea consultar: ")
        for key, value in inventario.items():
            if key == producto:
                print(f"Stock actual de {key}: {value}")
                break
        else:
            print(f"El producto {producto} no se encuentra en el inventario")
    elif eleccion == "2":
        producto = input("Ingrese el nombre del producto al que desea agregar unidades: ")
        for key, value in inventario.items():
            if key == producto:
                cantidad = int(input("Ingrese la cantidad de unidades que desea agregar: "))
                inventario[key] += cantidad
                print(f"Nuevo stock de {key}: {inventario[key]}")
                break
        else:
            print(f"El producto {producto} no se encuentra en el inventario")
    elif eleccion == "3":
        producto = input("Ingrese el nombre del producto al que desea quitar unidades: ")
        for key, value in inventario.items():
            if key == producto:
                cantidad = int(input("Ingrese la cantidad de unidades que desea quitar: "))
                if cantidad <= inventario[key]:
                    inventario[key] -= cantidad
                    print(f"Nuevo stock de {key}: {inventario[key]}")
                else:
                    print(f"No hay suficientes unidades de {key} en el inventario")
                break
        else:
            print(f"El producto {producto} no se encuentra en el inventario")
    elif eleccion == "4":
        producto = input("Ingrese el nombre del producto que desea agregar: ")
        cantidad = int(input("Ingrese la cantidad de unidades del producto: "))
        inventario.update({producto: cantidad})
        print(f"El producto {producto} ha sido agregado al inventario con {cantidad} unidades")
    elif eleccion == "5":
        print("Inventario completo:")
        for key, value in inventario.items():
            print(f"{key}: {value}")
    elif eleccion == "6":
        print("Saliendo del programa...")
        programa = False