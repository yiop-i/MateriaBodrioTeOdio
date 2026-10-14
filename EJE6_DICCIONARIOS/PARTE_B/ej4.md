# Manejo de JSON

Los objetos JSON (JavaScript Object Notation) son objetos que se utilizan para comunicar información entre aplicaciones, clientes y servidores y demás. Pueden ser interpretados dentro de Python como un diccionario. 

Vamos a simular una respuesta de una página web guardada en el archivo *payload.json*. Vamos a abrir este archivo y obtener sus contenidos a través de un manejador de contextos.

Debemos copiar y pegar el siguiente código:

'''
import json

with open("payload.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

print(datos)
'''

Una vez cargados los datos (estarán en forma de un diccionario almacenado en la variable 'archivo'), analizar los valores dentro de cada nivel. 

'''
print(datos["usuario"]["nombre"])
print(datos["curso"]["docente"]["email"])
print(datos["asistencia"]["porcentaje"])
'''

Imprimir el nombre del usuario que se ha devuelto.
Imprimir el correo electrónico del docente.
Imprimir el porcentaje de asistencias.