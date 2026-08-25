# Guía: Cómo ubicarse y moverse entre directorios en Windows

## 1. ¿Cómo están organizados los archivos en una computadora?

Cuando utilizamos una computadora, constantemente trabajamos con archivos:

* Documentos.
* Imágenes.
* Videos.
* Programas.
* Código fuente.
* Archivos de configuración.

Para poder encontrarlos y organizarlos, el sistema operativo utiliza una **estructura de directorios**.

Un directorio es lo que normalmente conocemos como una **carpeta**.

Por ejemplo:

```text
Documentos
│
├── Tareas
│   ├── tarea1.docx
│   └── tarea2.docx
│
├── Fotos
│   └── vacaciones.jpg
│
└── Programación
    ├── Python
    └── Arduino
```

Podemos imaginar el sistema de archivos como un árbol.

Existe un punto de inicio y, a partir de él, se encuentran diferentes carpetas que pueden contener:

* Archivos.
* Otras carpetas.

Por eso decimos que las carpetas pueden estar **dentro de otras carpetas**.

---

# 2. Las unidades de almacenamiento

En Windows, los dispositivos de almacenamiento se organizan mediante letras.

La unidad principal normalmente se llama:

```text
C:
```

Por ejemplo, podemos tener:

```text
C:\
```

El símbolo `\` representa una separación entre directorios.

Dentro de la unidad `C:` existen muchas carpetas:

```text
C:\
├── Windows
├── Program Files
├── Program Files (x86)
└── Users
```

Una ruta completa podría ser:

```text
C:\Users\Juan\Documents
```

Esto significa:

1. Estamos en la unidad `C:`.
2. Dentro de ella entramos a `Users`.
3. Dentro de `Users` entramos a `Juan`.
4. Dentro de `Juan` entramos a `Documents`.

A esto lo llamamos una **ruta** o **path**.

---

# 3. ¿Qué es una ruta?

Una ruta indica la ubicación de un archivo o directorio dentro del sistema.

Por ejemplo:

```text
C:\Users\Juan\Documents\Programacion\Proyecto
```

Podemos interpretarla como:

```text
C:\
 └── Users
      └── Juan
           └── Documents
                └── Programacion
                     └── Proyecto
```

La ruta nos permite saber exactamente dónde se encuentra algo.

Por ejemplo, si tenemos un archivo llamado:

```text
main.py
```

Su ubicación completa podría ser:

```text
C:\Users\Juan\Documents\Programacion\Proyecto\main.py
```

Esta es su **ruta absoluta**.

---

# 4. Rutas absolutas y rutas relativas

Existen dos formas principales de indicar una ubicación.

## Ruta absoluta

Una ruta absoluta comienza desde una unidad o punto de inicio del sistema.

Ejemplo:

```text
C:\Users\Juan\Documents\Programacion
```

No importa dónde estemos ubicados actualmente: esta ruta siempre indica el mismo lugar.

---

## Ruta relativa

Una ruta relativa depende del lugar en el que estamos actualmente.

Supongamos que estamos en:

```text
C:\Users\Juan\Documents
```

Y dentro de `Documents` existe una carpeta llamada:

```text
Programacion
```

Podemos referirnos a ella simplemente como:

```text
Programacion
```

Porque ya estamos dentro del directorio anterior.

Esto es una ruta relativa.

---

# 5. ¿Qué significa "estar parado" en un directorio?

Este es uno de los conceptos más importantes para trabajar con la terminal.

Cuando abrimos una terminal, la computadora necesita saber:

> ¿Desde qué lugar del sistema de archivos voy a trabajar?

Ese lugar se llama:

* Directorio actual.
* Directorio de trabajo.
* *Current Working Directory*.

De manera informal solemos decir:

> Estamos "parados" en un directorio.

Por ejemplo, si la terminal muestra:

```text
C:\Users\Juan>
```

Significa que actualmente estamos trabajando dentro de:

```text
C:\Users\Juan
```

No significa simplemente que esa carpeta existe.

Significa que:

> Los comandos que ejecutemos interpretarán las rutas relativas tomando este directorio como punto de referencia.

---

# 6. Una analogía: estar parado en una ciudad

Imaginemos que estamos utilizando instrucciones para movernos por una ciudad.

Si alguien nos dice:

> Ve dos cuadras hacia adelante.

Necesitamos saber primero:

> ¿Desde dónde estoy parado?

La misma instrucción puede llevarnos a lugares diferentes dependiendo de nuestra posición inicial.

En una terminal sucede lo mismo.

Supongamos esta estructura:

```text
Documentos
│
├── ProyectoA
│   └── archivo.py
│
└── ProyectoB
    └── programa.py
```

Si estamos parados en:

```text
Documentos
```

Y escribimos:

```text
ProyectoA
```

Nos estamos refiriendo a:

```text
Documentos\ProyectoA
```

Pero si estamos parados en otro lugar, por ejemplo:

```text
C:\Users\Juan
```

La computadora buscará:

```text
C:\Users\Juan\ProyectoA
```

Por lo tanto, el mismo nombre puede significar ubicaciones diferentes dependiendo del directorio actual.

---

# 7. La terminal de Windows

Windows posee diferentes terminales.

Algunas de las más utilizadas son:

* Símbolo del sistema o Command Prompt (`cmd`).
* PowerShell.
* Windows Terminal.

En esta guía utilizaremos principalmente comandos que permiten entender el concepto de navegación.

Cuando abrimos una terminal podemos ver algo similar a:

```text
C:\Users\Juan>
```

Esto nos indica nuestra ubicación actual.

Estamos parados en:

```text
C:\Users\Juan
```

---

# 8. Ver dónde estamos

En PowerShell podemos utilizar:

```powershell
pwd
```

Esto significa:

```text
Print Working Directory
```

Es decir:

> Mostrar el directorio de trabajo actual.

El resultado podría ser:

```text
Path
----
C:\Users\Juan
```

Esto nos confirma que estamos parados en:

```text
C:\Users\Juan
```

---

# 9. Ver qué hay dentro del directorio

Una vez que sabemos dónde estamos, podemos preguntar:

> ¿Qué archivos y carpetas existen aquí?

En PowerShell podemos utilizar:

```powershell
dir
```

o:

```powershell
ls
```

Por ejemplo:

```text
Directorio: C:\Users\Juan

Desktop
Documents
Downloads
Pictures
```

Esto significa que dentro del directorio actual existen esas carpetas.

Podemos representarlo así:

```text
C:\Users\Juan
│
├── Desktop
├── Documents
├── Downloads
└── Pictures
```

---

# 10. Movernos a otro directorio con `cd`

El comando principal para movernos entre directorios es:

```text
cd
```

Su nombre proviene de:

```text
Change Directory
```

Es decir:

> Cambiar de directorio.

Supongamos que estamos en:

```text
C:\Users\Juan
```

Y queremos entrar a:

```text
Documents
```

Escribimos:

```powershell
cd Documents
```

Ahora nuestra ubicación será:

```text
C:\Users\Juan\Documents
```

Podemos comprobarlo utilizando:

```powershell
pwd
```

---

# 11. Entrar a una carpeta dentro de otra carpeta

Supongamos la siguiente estructura:

```text
Documents
│
└── Programacion
    │
    └── Python
        │
        └── Proyecto
```

Si estamos parados en:

```text
C:\Users\Juan\Documents
```

Podemos entrar directamente a:

```text
Proyecto
```

utilizando:

```powershell
cd Programacion\Python\Proyecto
```

Ahora estaremos parados en:

```text
C:\Users\Juan\Documents\Programacion\Python\Proyecto
```

La terminal sigue cada parte de la ruta.

Primero entra en:

```text
Programacion
```

Luego:

```text
Python
```

Y finalmente:

```text
Proyecto
```

---

# 12. Subir un directorio con `..`

Existe una forma especial de referirse al directorio anterior.

Se utiliza:

```text
..
```

Esto significa:

> El directorio padre.

Supongamos que estamos en:

```text
C:\Users\Juan\Documents\Programacion
```

Podemos volver a:

```text
C:\Users\Juan\Documents
```

utilizando:

```powershell
cd ..
```

Podemos verlo gráficamente:

```text
Documents
│
└── Programacion
    ↑
   Estamos aquí
```

Cuando escribimos:

```powershell
cd ..
```

Subimos un nivel:

```text
Documents
↑
Estamos aquí
│
└── Programacion
```

---

# 13. Subir varios directorios

Supongamos que estamos en:

```text
C:\Users\Juan\Documents\Programacion\Python
```

Y queremos volver a:

```text
C:\Users\Juan\Documents
```

Podemos ejecutar:

```powershell
cd ..
```

dos veces.

También podemos indicar:

```powershell
cd ..\..
```

Esto significa:

```text
Python
  │
  └── ..
       │
       └── ..
```

Es decir, subir dos niveles.

---

# 14. El directorio actual: `.`

El símbolo:

```text
.
```

representa el directorio actual.

Por ejemplo, si estamos en:

```text
C:\Users\Juan\Documents\Proyecto
```

Entonces:

```text
.
```

significa:

```text
C:\Users\Juan\Documents\Proyecto
```

Podemos imaginarlo así:

```text
.
│
└── Aquí estoy actualmente
```

Este concepto será muy importante cuando trabajemos con programación, Git y otros comandos.

---

# 15. Resumen de los símbolos especiales

| Símbolo | Significado                  |
| ------- | ---------------------------- |
| `.`     | Directorio actual            |
| `..`    | Directorio padre             |
| `\`     | Separación entre directorios |
| `C:`    | Unidad de almacenamiento     |

Por ejemplo:

```text
C:\Users\Juan\Documents
```

indica una ruta absoluta.

Mientras que:

```text
.\Proyecto
```

indica:

> La carpeta `Proyecto` que está dentro del directorio donde estoy parado.

Y:

```text
..\Proyecto
```

indica:

> La carpeta `Proyecto` que está dentro del directorio padre.

---

# 16. Ejemplo completo de navegación

Supongamos la siguiente estructura:

```text
C:\
└── Users
    └── Juan
        └── Documents
            └── Programacion
                └── MiProyecto
                    ├── main.py
                    └── README.md
```

Abrimos PowerShell y comenzamos en:

```text
C:\Users\Juan
```

Primero verificamos dónde estamos:

```powershell
pwd
```

Luego vemos las carpetas disponibles:

```powershell
ls
```

Entramos a `Documents`:

```powershell
cd Documents
```

Luego:

```powershell
cd Programacion
```

Luego:

```powershell
cd MiProyecto
```

Ahora estamos parados en:

```text
C:\Users\Juan\Documents\Programacion\MiProyecto
```

Si ejecutamos:

```powershell
ls
```

veremos:

```text
main.py
README.md
```

Podemos volver a `Programacion` utilizando:

```powershell
cd ..
```

---

# 17. ¿Qué tiene que ver todo esto con Git?

Mucho.

Git trabaja sobre archivos que se encuentran organizados dentro del sistema de archivos.

Supongamos que tenemos:

```text
C:\Users\Juan\Documents\Programacion
```

Y clonamos un repositorio llamado:

```text
MiProyecto
```

Después de clonarlo tendremos algo parecido a:

```text
C:\Users\Juan\Documents\Programacion
│
└── MiProyecto
    ├── main.py
    ├── README.md
    └── .git
```

La carpeta:

```text
MiProyecto
```

es ahora un **repositorio Git**.

---

# 18. ¿Qué es realmente un repositorio?

Un repositorio es un directorio que contiene:

1. Los archivos de nuestro proyecto.
2. Información que Git utiliza para controlar las versiones del proyecto.

Una estructura simplificada sería:

```text
MiProyecto
│
├── main.py
├── README.md
│
└── .git
```

La carpeta especial:

```text
.git
```

contiene información interna utilizada por Git.

Por ejemplo, Git almacena información sobre:

* Commits.
* Ramas.
* Configuración.
* Historial.
* Referencias a diferentes versiones del proyecto.

Cuando Git encuentra esta información, puede identificar que estamos trabajando dentro de un repositorio.

---

# 19. Clonar un repositorio

Supongamos que queremos descargar un proyecto desde GitHub.

Podemos utilizar:

```powershell
git clone URL_DEL_REPOSITORIO
```

Por ejemplo:

```powershell
git clone https://github.com/usuario/proyecto.git
```

Si estamos parados en:

```text
C:\Users\Juan\Documents\Programacion
```

y ejecutamos el comando anterior, Git creará normalmente una nueva carpeta:

```text
C:\Users\Juan\Documents\Programacion\proyecto
```

Entonces tendremos:

```text
Programacion
│
└── proyecto
    ├── archivos del proyecto
    └── .git
```

---

# 20. Entrar al repositorio

Después de clonar el repositorio, debemos movernos dentro de él:

```powershell
cd proyecto
```

Ahora estamos parados en:

```text
C:\Users\Juan\Documents\Programacion\proyecto
```

Ahora podemos ejecutar:

```powershell
git status
```

Git responderá mostrando información sobre el estado del repositorio.

Por ejemplo:

```text
On branch main
nothing to commit, working tree clean
```

¿Por qué funciona?

Porque Git puede encontrar la información del repositorio.

---

# 21. ¿Por qué importa dónde estamos parados cuando usamos Git?

Supongamos que tenemos:

```text
C:\Users\Juan\Documents
│
└── Programacion
    │
    └── MiRepositorio
        ├── main.py
        └── .git
```

Si estamos parados en:

```text
C:\Users\Juan\Documents
```

y ejecutamos:

```powershell
git status
```

Git puede no encontrar un repositorio y devolver un error similar a:

```text
fatal: not a git repository
```

Esto ocurre porque el directorio actual no contiene la información necesaria para identificar el proyecto como un repositorio Git.

En cambio, si hacemos:

```powershell
cd Programacion\MiRepositorio
```

y luego ejecutamos:

```powershell
git status
```

Git puede encontrar:

```text
.git
```

y reconocer el repositorio.

---

# 22. Una idea importante: Git utiliza el contexto del directorio

Cuando ejecutamos:

```powershell
git status
```

en realidad estamos diciendo algo parecido a:

> Git, analiza el repositorio relacionado con el directorio donde estoy trabajando.

Por eso nuestra ubicación importa.

La terminal necesita saber:

```text
¿Dónde estoy?
```

Git necesita saber:

```text
¿Sobre qué proyecto estoy trabajando?
```

La ubicación actual permite responder ambas preguntas.

---

# 23. Trabajar dentro de subdirectorios de un repositorio

Supongamos que nuestro repositorio tiene esta estructura:

```text
MiRepositorio
│
├── .git
├── README.md
├── src
│   ├── main.py
│   └── utils.py
│
└── tests
    └── test_main.py
```

Estamos parados dentro de:

```text
MiRepositorio
```

Ejecutamos:

```powershell
git status
```

Git funciona correctamente.

Ahora entramos a:

```text
src
```

utilizando:

```powershell
cd src
```

Ahora estamos en:

```text
MiRepositorio\src
```

Si ejecutamos nuevamente:

```powershell
git status
```

Git también puede funcionar.

¿Por qué?

Porque seguimos estando dentro del repositorio.

Aunque la carpeta `.git` se encuentra en:

```text
MiRepositorio\.git
```

Git puede identificar que el directorio actual pertenece a un proyecto cuyo directorio principal se encuentra más arriba.

Podemos representarlo así:

```text
MiRepositorio
│
├── .git
│
└── src
    ↑
 Estamos aquí
```

Git puede subir desde:

```text
src
```

hasta encontrar:

```text
.git
```

---

# 24. Pero si salimos del repositorio...

Supongamos que estamos en:

```text
C:\Users\Juan\Documents\Programacion\MiRepositorio
```

Y ejecutamos:

```powershell
cd ..
```

Ahora estamos en:

```text
C:\Users\Juan\Documents\Programacion
```

Nuestra estructura es:

```text
Programacion
│
├── OtroProyecto
│
└── MiRepositorio
    └── .git
```

Ahora estamos parados aquí:

```text
Programacion
↑
Estamos aquí
│
└── MiRepositorio
    └── .git
```

Si ejecutamos:

```powershell
git status
```

Git ya no está trabajando dentro de `MiRepositorio`.

Por lo tanto, no puede utilizar automáticamente ese repositorio.

Debemos volver a entrar:

```powershell
cd MiRepositorio
```

---

# 25. Ejemplo práctico completo con GitHub

Supongamos que queremos trabajar con un repositorio llamado:

```text
mi-proyecto
```

Primero elegimos dónde queremos guardarlo.

Por ejemplo:

```text
C:\Users\Juan\Documents\Programacion
```

Nos movemos allí:

```powershell
cd C:\Users\Juan\Documents\Programacion
```

Verificamos nuestra ubicación:

```powershell
pwd
```

Luego clonamos:

```powershell
git clone URL_DEL_REPOSITORIO
```

Ahora vemos las carpetas:

```powershell
ls
```

Aparece:

```text
mi-proyecto
```

Entramos al repositorio:

```powershell
cd mi-proyecto
```

Ahora estamos parados dentro del proyecto.

Podemos verificar:

```powershell
git status
```

También podemos ver las ramas:

```powershell
git branch
```

Podemos descargar cambios:

```powershell
git pull
```

Y podemos agregar cambios:

```powershell
git add .
```

El comando:

```powershell
git add .
```

significa aproximadamente:

> Agrega a Git los cambios realizados en el directorio actual y sus subdirectorios.

Aquí aparece nuevamente el concepto de:

```text
.
```

El punto representa:

```text
El directorio actual.
```

Por lo tanto, nuestra ubicación vuelve a ser importante.

---

# 26. La idea central

Cada vez que utilizamos una terminal debemos pensar:

> ¿Dónde estoy parado?

Antes de ejecutar un comando, conviene verificar:

```powershell
pwd
```

Y observar el contenido:

```powershell
ls
```

Luego podemos decidir hacia dónde movernos utilizando:

```powershell
cd nombre_de_carpeta
```

Para volver atrás:

```powershell
cd ..
```

Para trabajar con Git, debemos recordar que un repositorio ocupa una ubicación concreta dentro del sistema de archivos.

Por ejemplo:

```text
C:\Users\Juan\Documents\Programacion\MiRepositorio
```

Si queremos trabajar sobre ese proyecto, debemos movernos hacia él:

```powershell
cd C:\Users\Juan\Documents\Programacion\MiRepositorio
```

Una vez dentro, Git puede identificar el repositorio y trabajar sobre sus archivos.

---

# 27. Mapa mental final

Podemos resumir todo el proceso de esta manera:

```text
COMPUTADORA
│
└── Unidad C:
    │
    └── Users
        │
        └── Usuario
            │
            └── Documents
                │
                └── Programacion
                    │
                    └── MiRepositorio
                        │
                        ├── .git
                        ├── README.md
                        └── main.py
```

La terminal siempre tiene una posición actual:

```text
¿Dónde estoy parado?
```

Podemos consultar:

```powershell
pwd
```

Podemos ver qué existe allí:

```powershell
ls
```

Podemos movernos:

```powershell
cd carpeta
```

Podemos subir:

```powershell
cd ..
```

Y cuando trabajamos con Git debemos asegurarnos de estar:

```text
Dentro del repositorio
```

o dentro de alguna de sus subcarpetas.

---

# 28. Ejercicio práctico

Supongamos la siguiente estructura:

```text
C:\
└── Users
    └── Alumno
        └── Documents
            └── Git
                └── proyecto-prueba
                    ├── .git
                    ├── README.md
                    └── src
                        └── main.py
```

Responde:

### 1.

Si estamos parados en:

```text
C:\Users\Alumno
```

¿Qué comando utilizarías para entrar a `Documents`?

---

### 2.

Si estamos en:

```text
C:\Users\Alumno\Documents
```

¿Qué comando utilizarías para entrar directamente a `main.py`?

**Pista:** No podemos "entrar" a un archivo utilizando `cd`. ¿A qué directorio debemos movernos para trabajar desde allí?

---

### 3.

Si estamos en:

```text
C:\Users\Alumno\Documents\Git\proyecto-prueba\src
```

¿Qué comando debemos utilizar para volver al directorio principal del repositorio?

---

### 4.

Si estamos parados en:

```text
C:\Users\Alumno\Documents\Git
```

¿Funcionaría correctamente `git status` para analizar el repositorio `proyecto-prueba`?

¿Por qué?

---

### 5.

Si estamos en:

```text
C:\Users\Alumno\Documents\Git\proyecto-prueba\src
```

¿Funcionaría `git status`?

¿Por qué?

---

## Regla de oro

Antes de ejecutar comandos en la terminal, especialmente comandos que pueden modificar archivos, debemos saber:

> **¿Dónde estoy parado y sobre qué archivos va a actuar este comando?**

Entender el directorio actual es una de las bases para trabajar correctamente con:

* Git.
* GitHub.
* Python.
* Compiladores.
* Node.js.
* Herramientas de desarrollo.
* Servidores.
* Sistemas Linux.

En la terminal, **el lugar desde el cual ejecutamos un comando forma parte del contexto del comando**.
