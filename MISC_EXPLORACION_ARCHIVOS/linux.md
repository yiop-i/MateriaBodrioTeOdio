# Guía: Cómo ubicarse y moverse entre directorios en Linux

## 1. ¿Cómo están organizados los archivos en Linux?

Al igual que en Windows, en Linux trabajamos constantemente con archivos:

* Documentos.
* Imágenes.
* Videos.
* Programas.
* Código fuente.
* Archivos de configuración.
* Archivos del propio sistema operativo.

Para organizar todos estos archivos, Linux utiliza un **sistema de archivos organizado en directorios**.

Un directorio es lo que normalmente conocemos como una **carpeta**.

Por ejemplo:

```text
Documentos
│
├── Tareas
│   ├── tarea1.txt
│   └── tarea2.txt
│
├── Fotos
│   └── vacaciones.jpg
│
└── Programacion
    ├── Python
    └── Arduino
```

Los directorios pueden contener:

* Archivos.
* Otros directorios.

Esto genera una estructura similar a un árbol.

```text
Directorio principal
│
├── Directorio A
│   ├── Archivo 1
│   └── Archivo 2
│
└── Directorio B
    └── Archivo 3
```

---

# 2. Una diferencia importante entre Windows y Linux

En Windows normalmente encontramos unidades representadas mediante letras:

```text
C:
D:
E:
```

Por ejemplo:

```text
C:\Users\Juan\Documents
```

En Linux, la estructura funciona de manera diferente.

Linux organiza todo el sistema de archivos a partir de un único punto llamado:

```text
/
```

Este símbolo se llama:

> **Directorio raíz**.

Todo lo que existe en el sistema se encuentra dentro de esta estructura.

Por ejemplo:

```text
/
├── home
├── etc
├── bin
├── usr
├── var
└── tmp
```

Podemos pensar en `/` como el punto más alto del árbol de directorios.

---

# 3. El directorio raíz `/`

La raíz del sistema es:

```text
/
```

Desde allí comienza toda la estructura.

Por ejemplo:

```text
/
├── home
│   ├── alumno1
│   └── alumno2
│
├── etc
│
├── usr
│
└── var
```

Es importante no confundir:

```text
/
```

con:

```text
\
```

En Windows normalmente se utiliza:

```text
\
```

como separador entre directorios.

Por ejemplo:

```text
C:\Users\Juan\Documents
```

En Linux se utiliza:

```text
/
```

Por ejemplo:

```text
/home/juan/Documentos
```

---

# 4. ¿Qué es una ruta?

Una **ruta** o *path* indica la ubicación de un archivo o directorio dentro del sistema.

Por ejemplo:

```text
/home/juan/Documentos/Programacion
```

Podemos interpretarla de la siguiente manera:

```text
/
└── home
    └── juan
        └── Documentos
            └── Programacion
```

Cada parte de la ruta indica que estamos entrando en un directorio.

Por ejemplo:

```text
/home
```

significa:

> Dentro de la raíz `/`, entrar al directorio `home`.

Luego:

```text
/home/juan
```

significa:

> Dentro de `/home`, entrar al directorio `juan`.

Y:

```text
/home/juan/Documentos
```

significa:

> Dentro de `/home/juan`, entrar al directorio `Documentos`.

---

# 5. El directorio personal

En Linux, cada usuario normalmente tiene su propio directorio personal.

Por ejemplo:

```text
/home/juan
```

o:

```text
/home/alumno
```

Dentro de ese directorio podemos encontrar nuestras carpetas personales:

```text
/home/juan
│
├── Documentos
├── Descargas
├── Imágenes
├── Música
└── Escritorio
```

El directorio:

```text
/home/juan
```

es nuestro espacio personal dentro del sistema.

En muchas distribuciones de Linux, cuando abrimos una terminal comenzamos directamente allí.

---

# 6. El símbolo `~`

Linux utiliza un símbolo especial para representar el directorio personal del usuario actual:

```text
~
```

Por ejemplo, si nuestro usuario se llama:

```text
juan
```

entonces:

```text
~
```

representa:

```text
/home/juan
```

Por lo tanto:

```text
~/Documentos
```

significa:

```text
/home/juan/Documentos
```

El símbolo `~` es muy utilizado porque permite escribir rutas sin tener que escribir el nombre completo del usuario.

---

# 7. ¿Qué significa "estar parado" en un directorio?

Este es uno de los conceptos más importantes para trabajar con Linux.

Cuando abrimos una terminal, el sistema necesita saber:

> ¿Desde qué lugar del sistema de archivos voy a trabajar?

Ese lugar se llama:

* Directorio actual.
* Directorio de trabajo.
* *Current Working Directory*.

Informalmente solemos decir:

> Estamos "parados" en un directorio.

Por ejemplo, si la terminal muestra:

```text
juan@computadora:~/Documentos$
```

significa que estamos trabajando dentro de:

```text
/home/juan/Documentos
```

La terminal no solamente nos muestra una ubicación.

También utiliza esa ubicación como contexto para interpretar muchos comandos.

---

# 8. Una analogía: estar parado en una ciudad

Imaginemos que una persona recibe la siguiente instrucción:

> Camina dos cuadras hacia adelante.

Para saber a dónde llegará, primero necesitamos conocer su posición actual.

La misma instrucción puede llevar a lugares diferentes dependiendo de dónde se encuentre la persona.

En Linux ocurre algo similar.

Supongamos la siguiente estructura:

```text
Documentos
│
├── ProyectoA
│   └── main.py
│
└── ProyectoB
    └── programa.py
```

Si estamos parados en:

```text
/home/juan/Documentos
```

y escribimos:

```text
ProyectoA
```

nos estamos refiriendo a:

```text
/home/juan/Documentos/ProyectoA
```

Pero si estamos parados en:

```text
/home/juan
```

entonces:

```text
ProyectoA
```

sería interpretado como:

```text
/home/juan/ProyectoA
```

La misma ruta relativa puede significar lugares diferentes dependiendo de dónde estamos parados.

---

# 9. Ver dónde estamos con `pwd`

Para saber exactamente dónde estamos ubicados utilizamos:

```bash
pwd
```

`pwd` significa:

```text
Print Working Directory
```

Es decir:

> Mostrar el directorio de trabajo actual.

Por ejemplo:

```bash
$ pwd
/home/juan/Documentos
```

Esto significa que estamos parados en:

```text
/home/juan/Documentos
```

Antes de ejecutar comandos importantes, especialmente cuando estamos aprendiendo, es una buena práctica preguntarse:

> ¿Dónde estoy?

Y ejecutar:

```bash
pwd
```

---

# 10. Ver qué existe dentro del directorio con `ls`

Una vez que sabemos dónde estamos, podemos preguntar:

> ¿Qué archivos y directorios existen aquí?

Para eso utilizamos:

```bash
ls
```

Por ejemplo:

```bash
$ ls
ProyectoA  ProyectoB  tarea.txt
```

Esto significa que dentro del directorio actual existen:

```text
/home/juan/Documentos
│
├── ProyectoA
├── ProyectoB
└── tarea.txt
```

Es importante comprender que:

```bash
ls
```

por sí solo muestra el contenido del directorio donde estamos parados.

---

# 11. Movernos entre directorios con `cd`

El comando principal para movernos entre directorios es:

```bash
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
/home/juan
```

Y queremos entrar a:

```text
Documentos
```

Ejecutamos:

```bash
cd Documentos
```

Ahora estamos en:

```text
/home/juan/Documentos
```

Podemos comprobarlo utilizando:

```bash
pwd
```

---

# 12. Entrar a varios directorios

Supongamos que tenemos:

```text
/home/juan
└── Documentos
    └── Programacion
        └── Python
            └── Proyecto
```

Si estamos en:

```text
/home/juan
```

podemos entrar directamente al proyecto utilizando:

```bash
cd Documentos/Programacion/Python/Proyecto
```

Ahora estamos parados en:

```text
/home/juan/Documentos/Programacion/Python/Proyecto
```

La terminal sigue cada parte de la ruta.

Primero:

```text
Documentos
```

Luego:

```text
Programacion
```

Después:

```text
Python
```

Y finalmente:

```text
Proyecto
```

---

# 13. Subir un directorio con `..`

Existe una forma especial de referirse al directorio anterior.

Se utiliza:

```text
..
```

Esto significa:

> El directorio padre.

Supongamos que estamos en:

```text
/home/juan/Documentos/Programacion
```

Podemos volver a:

```text
/home/juan/Documentos
```

utilizando:

```bash
cd ..
```

Podemos representarlo así:

```text
Documentos
│
└── Programacion
    ↑
Estamos aquí
```

Después de ejecutar:

```bash
cd ..
```

subimos:

```text
Documentos
↑
Estamos aquí
│
└── Programacion
```

---

# 14. Subir varios directorios

Supongamos que estamos en:

```text
/home/juan/Documentos/Programacion/Python
```

Y queremos volver a:

```text
/home/juan/Documentos
```

Podemos ejecutar:

```bash
cd ..
cd ..
```

También podemos escribir:

```bash
cd ../..
```

Esto significa:

> Subir dos niveles.

Podemos continuar agregando:

```text
..
```

para subir más niveles.

Por ejemplo:

```bash
cd ../../..
```

sube tres niveles.

---

# 15. El directorio actual: `.`

El símbolo:

```text
.
```

representa:

> El directorio actual.

Supongamos que estamos en:

```text
/home/juan/Documentos/Proyecto
```

Entonces:

```text
.
```

significa:

```text
/home/juan/Documentos/Proyecto
```

Podemos imaginarlo como:

```text
.
│
└── Aquí estoy actualmente
```

Este símbolo aparece constantemente cuando trabajamos en Linux y programación.

Por ejemplo:

```bash
./programa
```

significa:

> Ejecutar el archivo `programa` que se encuentra en el directorio actual.

---

# 16. Resumen de los símbolos especiales

| Símbolo | Significado                             |
| ------- | --------------------------------------- |
| `/`     | Directorio raíz o separador en una ruta |
| `.`     | Directorio actual                       |
| `..`    | Directorio padre                        |
| `~`     | Directorio personal del usuario         |

Por ejemplo:

```text
/home/juan
```

es una ruta absoluta.

Mientras que:

```text
./Proyecto
```

significa:

> La carpeta `Proyecto` que está dentro del directorio actual.

Y:

```text
../Proyecto
```

significa:

> La carpeta `Proyecto` que está dentro del directorio padre.

---

# 17. Rutas absolutas y rutas relativas

Este concepto es fundamental.

## Ruta absoluta

Una ruta absoluta comienza desde la raíz:

```text
/
```

Por ejemplo:

```text
/home/juan/Documentos/Programacion
```

Esta ruta siempre representa la misma ubicación, independientemente de dónde estemos parados.

---

## Ruta relativa

Una ruta relativa depende del directorio actual.

Supongamos que estamos en:

```text
/home/juan/Documentos
```

Si escribimos:

```text
Programacion
```

nos referimos a:

```text
/home/juan/Documentos/Programacion
```

Pero si estamos en:

```text
/home/juan
```

esa misma ruta:

```text
Programacion
```

significaría:

```text
/home/juan/Programacion
```

Por lo tanto:

> Una ruta relativa necesita conocer el lugar desde el que estamos trabajando.

---

# 18. Volver al directorio personal

En Linux podemos volver al directorio personal utilizando:

```bash
cd
```

sin indicar ningún directorio.

También podemos utilizar:

```bash
cd ~
```

Por ejemplo, si estamos en:

```text
/home/juan/Documentos/Programacion/Python
```

y ejecutamos:

```bash
cd
```

volveremos normalmente a:

```text
/home/juan
```

---

# 19. Ejemplo completo de navegación

Supongamos la siguiente estructura:

```text
/
└── home
    └── juan
        └── Documentos
            └── Programacion
                └── MiProyecto
                    ├── main.py
                    └── README.md
```

Abrimos la terminal.

Comenzamos en:

```text
/home/juan
```

Verificamos:

```bash
pwd
```

Vemos qué existe:

```bash
ls
```

Entramos a:

```bash
cd Documentos
```

Luego:

```bash
cd Programacion
```

Luego:

```bash
cd MiProyecto
```

Ahora estamos parados en:

```text
/home/juan/Documentos/Programacion/MiProyecto
```

Podemos ejecutar:

```bash
ls
```

y veremos:

```text
main.py
README.md
```

Para volver a `Programacion`:

```bash
cd ..
```

---

# 20. Directorios ocultos

En Linux, muchos archivos y directorios que comienzan con un punto son considerados ocultos.

Por ejemplo:

```text
.git
```

Si ejecutamos:

```bash
ls
```

normalmente no veremos:

```text
.git
```

Para ver también los archivos ocultos utilizamos:

```bash
ls -a
```

La opción:

```text
-a
```

significa aproximadamente:

> Mostrar todos los archivos.

Entonces podríamos ver:

```text
.
..
.git
README.md
main.py
```

Observamos tres elementos importantes:

```text
.
```

El directorio actual.

```text
..
```

El directorio padre.

Y:

```text
.git
```

Un directorio oculto utilizado por Git.

---

# 21. ¿Qué tiene que ver todo esto con Git?

Mucho.

Git trabaja sobre archivos organizados dentro del sistema de archivos.

Supongamos que tenemos:

```text
/home/juan/Documentos/Programacion
```

Y clonamos un repositorio llamado:

```text
MiProyecto
```

Después de clonarlo tendremos algo parecido a:

```text
/home/juan/Documentos/Programacion
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

# 22. ¿Qué es realmente un repositorio Git?

Un repositorio Git es un directorio que contiene:

1. Los archivos de nuestro proyecto.
2. Información utilizada por Git para controlar las versiones.

Simplificadamente:

```text
MiProyecto
│
├── main.py
├── README.md
│
└── .git
```

El directorio:

```text
.git
```

contiene información utilizada internamente por Git.

Por ejemplo:

* Historial de commits.
* Información sobre ramas.
* Configuración.
* Referencias.
* Información necesaria para reconstruir versiones anteriores.

Cuando Git encuentra este directorio, puede reconocer que estamos trabajando dentro de un repositorio.

---

# 23. Clonar un repositorio

Supongamos que queremos descargar un repositorio desde GitHub.

Primero elegimos dónde queremos guardarlo.

Por ejemplo:

```text
/home/juan/Documentos/Programacion
```

Nos movemos allí:

```bash
cd ~/Documentos/Programacion
```

Comprobamos dónde estamos:

```bash
pwd
```

Luego clonamos:

```bash
git clone URL_DEL_REPOSITORIO
```

Por ejemplo:

```bash
git clone https://github.com/usuario/proyecto.git
```

Git creará normalmente un directorio:

```text
proyecto
```

Nuestra estructura quedará:

```text
Programacion
│
└── proyecto
    ├── archivos del proyecto
    └── .git
```

---

# 24. Entrar al repositorio

Después de clonar el repositorio debemos movernos dentro de él:

```bash
cd proyecto
```

Ahora estamos parados en:

```text
/home/juan/Documentos/Programacion/proyecto
```

Podemos ejecutar:

```bash
git status
```

Git mostrará información sobre el estado del repositorio.

Por ejemplo:

```text
On branch main
nothing to commit, working tree clean
```

---

# 25. ¿Por qué importa dónde estamos parados cuando usamos Git?

Supongamos que tenemos:

```text
/home/juan/Documentos
│
└── Programacion
    │
    └── MiRepositorio
        ├── main.py
        └── .git
```

Si estamos parados en:

```text
/home/juan/Documentos
```

y ejecutamos:

```bash
git status
```

Git puede devolver:

```text
fatal: not a git repository
```

¿Por qué?

Porque desde el directorio actual Git no puede encontrar un repositorio asociado.

En cambio, si hacemos:

```bash
cd Programacion/MiRepositorio
```

y luego:

```bash
git status
```

Git encuentra:

```text
.git
```

y reconoce el repositorio.

---

# 26. Trabajar dentro de subdirectorios de un repositorio

Supongamos la siguiente estructura:

```text
MiRepositorio
│
├── .git
├── README.md
│
├── src
│   ├── main.py
│   └── utils.py
│
└── tests
    └── test_main.py
```

Estamos inicialmente en:

```text
MiRepositorio
```

Ejecutamos:

```bash
git status
```

Funciona correctamente.

Ahora entramos en:

```bash
cd src
```

Nuestra ubicación pasa a ser:

```text
MiRepositorio/src
```

Si ejecutamos:

```bash
git status
```

también funciona.

¿Por qué?

Porque seguimos estando dentro del repositorio.

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

Git puede buscar desde:

```text
src
```

hacia arriba en la estructura de directorios hasta encontrar:

```text
.git
```

Por eso Git reconoce que seguimos trabajando dentro del mismo proyecto.

---

# 27. ¿Qué ocurre cuando salimos del repositorio?

Supongamos que estamos en:

```text
/home/juan/Documentos/Programacion/MiRepositorio
```

Ejecutamos:

```bash
cd ..
```

Ahora estamos en:

```text
/home/juan/Documentos/Programacion
```

La estructura sería:

```text
Programacion
│
├── OtroProyecto
│
└── MiRepositorio
    └── .git
```

Estamos parados aquí:

```text
Programacion
↑
Estamos aquí
│
└── MiRepositorio
    └── .git
```

Si ejecutamos:

```bash
git status
```

Git no puede utilizar automáticamente `MiRepositorio`.

Debemos volver a entrar:

```bash
cd MiRepositorio
```

---

# 28. El directorio actual y los comandos

Este concepto no es importante únicamente para Git.

Muchos comandos dependen de dónde estamos parados.

Supongamos que tenemos:

```text
Proyecto
│
├── main.py
├── datos.csv
└── README.md
```

Si estamos dentro de:

```text
Proyecto
```

podemos ejecutar un programa utilizando:

```bash
python main.py
```

La terminal buscará:

```text
main.py
```

dentro del directorio actual.

Si estamos en otro directorio, el mismo comando puede fallar porque el archivo no se encuentra allí.

Por eso debemos pensar siempre:

> ¿Dónde estoy parado?

---

# 29. El significado de `./`

En Linux es muy común encontrar:

```text
./
```

Esto significa:

> Desde el directorio actual.

Por ejemplo:

```bash
./programa
```

significa:

> Ejecutar `programa` que se encuentra dentro del directorio actual.

Supongamos:

```text
Proyecto
│
└── programa
```

Estamos parados en:

```text
Proyecto
```

Entonces:

```bash
./programa
```

indica:

```text
Proyecto/programa
```

El punto representa nuestra posición actual.

---

# 30. `git add .` y el directorio actual

Uno de los comandos más utilizados en Git es:

```bash
git add .
```

Aquí:

```text
.
```

significa:

> El directorio actual.

Por lo tanto, el comando indica aproximadamente:

> Agrega al área de preparación los cambios encontrados desde el directorio actual y sus subdirectorios.

Supongamos:

```text
MiRepositorio
│
├── main.py
│
└── src
    └── programa.py
```

Si estamos parados en:

```text
MiRepositorio
```

y ejecutamos:

```bash
git add .
```

Git considera los cambios del proyecto desde ese punto.

Por eso debemos comprender qué representa:

```text
.
```

No es simplemente un carácter.

Representa:

> El lugar del sistema de archivos en el que estamos actualmente.

---

# 31. Ejemplo práctico completo con GitHub

Supongamos que queremos trabajar con un repositorio llamado:

```text
mi-proyecto
```

Primero elegimos dónde guardarlo:

```text
/home/juan/Documentos/Programacion
```

Nos movemos allí:

```bash
cd ~/Documentos/Programacion
```

Comprobamos nuestra ubicación:

```bash
pwd
```

Luego clonamos:

```bash
git clone URL_DEL_REPOSITORIO
```

Después vemos qué se creó:

```bash
ls
```

Aparece:

```text
mi-proyecto
```

Entramos:

```bash
cd mi-proyecto
```

Ahora estamos dentro del repositorio.

Podemos comprobarlo:

```bash
git status
```

Podemos ver ramas:

```bash
git branch
```

Podemos descargar cambios:

```bash
git pull
```

Podemos agregar cambios:

```bash
git add .
```

Y podemos verificar nuevamente:

```bash
git status
```

Todo esto funciona sobre el repositorio relacionado con nuestra ubicación actual.

---

# 32. Mapa mental final

Podemos representar todo el sistema así:

```text
/
│
└── home
    │
    └── juan
        │
        └── Documentos
            │
            └── Programacion
                │
                └── MiRepositorio
                    │
                    ├── .git
                    ├── README.md
                    └── main.py
```

La terminal siempre tiene una ubicación actual.

Debemos preguntarnos:

```text
¿Dónde estoy parado?
```

Podemos comprobarlo:

```bash
pwd
```

Podemos ver qué existe allí:

```bash
ls
```

Podemos entrar en una carpeta:

```bash
cd carpeta
```

Podemos subir:

```bash
cd ..
```

Podemos volver a nuestro directorio personal:

```bash
cd
```

Y podemos trabajar con rutas completas:

```bash
cd /home/juan/Documentos/Programacion/MiRepositorio
```

---

# 33. Tabla de comparación rápida: Windows y Linux

| Concepto                     | Windows             | Linux           |
| ---------------------------- | ------------------- | --------------- |
| Separador                    | `\`                 | `/`             |
| Punto inicial                | `C:\`               | `/`             |
| Directorio actual            | `.`                 | `.`             |
| Directorio padre             | `..`                | `..`            |
| Directorio personal          | `C:\Users\Usuario`  | `/home/usuario` |
| Atajo al directorio personal | Variable o ruta     | `~`             |
| Ver ubicación                | `pwd` en PowerShell | `pwd`           |
| Ver archivos                 | `dir` o `ls`        | `ls`            |
| Cambiar directorio           | `cd`                | `cd`            |

---

# 34. Ejercicio práctico

Supongamos la siguiente estructura:

```text
/
└── home
    └── alumno
        └── Documentos
            └── Git
                └── proyecto-prueba
                    ├── .git
                    ├── README.md
                    │
                    └── src
                        └── main.py
```

## Pregunta 1

Si estamos en:

```text
/home/alumno
```

¿Qué comando utilizaríamos para entrar a:

```text
Documentos
```

---

## Pregunta 2

Si estamos en:

```text
/home/alumno/Documentos
```

¿Qué comando podríamos utilizar para entrar directamente al directorio:

```text
src
```

del proyecto?

---

## Pregunta 3

Si estamos en:

```text
/home/alumno/Documentos/Git/proyecto-prueba/src
```

¿Qué comando utilizaríamos para volver al directorio principal del repositorio?

---

## Pregunta 4

Si estamos parados en:

```text
/home/alumno/Documentos/Git
```

y ejecutamos:

```bash
git status
```

¿Funcionará sobre el repositorio `proyecto-prueba`?

¿Por qué?

---

## Pregunta 5

Si estamos parados en:

```text
/home/alumno/Documentos/Git/proyecto-prueba/src
```

y ejecutamos:

```bash
git status
```

¿Funcionará?

¿Por qué?

---

## Pregunta 6

Si estamos en:

```text
/home/alumno/Documentos/Git/proyecto-prueba
```

¿Qué representa:

```text
.
```

?

¿Y qué representa:

```text
..
```

?

---

# Regla de oro

Antes de ejecutar un comando en Linux, especialmente comandos que pueden modificar o eliminar archivos, debemos preguntarnos:

> **¿Dónde estoy parado y sobre qué archivos va a actuar este comando?**

Para responder la primera pregunta utilizamos:

```bash
pwd
```

Para responder la segunda podemos utilizar:

```bash
ls
```

y analizar qué contiene el directorio.

Comprender el directorio actual es fundamental para trabajar con:

* Git.
* GitHub.
* Python.
* C y C++.
* Compiladores.
* Node.js.
* Servidores.
* Docker.
* Bash.
* Herramientas de administración de sistemas.

La idea fundamental es:

> **La terminal siempre trabaja desde algún lugar del sistema de archivos. Ese lugar forma parte del contexto desde el cual se interpretan muchos comandos.**

Antes de ejecutar un comando, conviene detenerse un momento y preguntarse:

```text
¿Dónde estoy?
```

Y si tenemos dudas:

```bash
pwd
```

Porque entender dónde estamos parados es el primer paso para entender qué estamos haciendo.
