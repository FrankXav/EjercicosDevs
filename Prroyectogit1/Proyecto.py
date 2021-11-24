import time
import os
from funciones import Mostarinfo
from funciones import Quitarresp
from funciones import formpreg
Comprendio=1
while(Comprendio!=0):   
    print('''Proyecto Git
        Bienvenido!!!! 
        Este es un programa diseñado para que cualquiera pueda aprender y entender los comandos 
        basico de git. Pero hay algunos puntos importantes para tomar en cuenta antes de comenzar
        1.- Lee bien la informacion y las instrucciones al momentoo de resolver un ejercicio
        2.- Es importante que intentes contestar con lo que recuerdes antes de pedir la pista o la respuesta
        3.- Repite la ejecucion de este programa las veces que sean necesarias
        4.- Exprimenta con una propia carpeta''')
    Comprendio=int(input("\nPrimera pregunta ¿Cuantas veces se menciono a la vaca en el texto?: "))
    if(Comprendio!=0):
        print("\n Claramente no leiste las instrucciones, Vuelve a leer e inteta de nuevo :(")
        time.sleep(4)

os.system("cls")
print("Bien!!!! Estas lsit@ para empezar")
print('''
Primero que todo ¿Que es Git?
Git es un sistema de control de versiones distribuido, gratuito y de código abierto, diseñado para gestionar 
desde proyectos pequeños a muy grandes con rapidez y eficacia.
La principal diferencia entre Git y cualquier cotro sitema de control de versiones es cómo Git modela sus datos.
Git modela sus datos más como un conjunto de instantáneas de un mini sistema de archivos. Cada vez que confirmas 
un cambio, o guardas el estado de tu proyecto en Git, él básicamente hace una foto del aspecto de todos tus 
archivos en ese momento, y guarda una referencia a esa instantánea.\n''')

pregunta1 = Quitarresp(input("En pocas palabras que es Git?: "))

if(not ("control de versiones" in pregunta1)):
    print("\nLa respuesta es 'Es un sitema de control de versiones que modela sus datos como un conjunto de instantaneas'")
    time.sleep(5)

texto1='''Bien ahora que ya sabemos que es git hablaremos de los principales comandos
    git init:
    Supongamos que esta trabajando en una aplicacion y desea subir sus avances a git para 
    tener disponible su trabajo en cualquier lugar y en todo momento
    Lo primero que tendriamos que hacer es abrir la terminal bash de git desde la
    carpeta donde se encuentra el proyecto y escribir "git init".
    Esto crea un nuevo subdirectorio llamado .git que contiene todos los archivos necesarios 
    del repositorio — un esqueleto de un repositorio Git.'''
Mostarinfo(texto1)

texto2='''git add:
    Ahora que ya inicio el reposiorio local, necesitamos agregar todos los archivos con los que hemos 
    trabajado hasta ahora para ello ocupamos "git add"
    Supongamos que nuestro proyecto ocupamos scripts de python y entre ellos tenemos uno llamado "Menu.py"
    y lo queremos agregar al repositorio
    Ocupariamos "git add Menu.py"
    Otra opcion es agregar todos los scripts de python con una sola instruccion "git add *.py"
    Asi todos los archivos que se encuentren en la carpeta donde nos estamos se agregaran al reposiorio
    y si tenemos muchos archivos de diferente tipo y ademas en distintos directorios podriamos ocupar:
    "git add ." y se agregaran todos los archivos (tambien los que estan dentro de otros directorios
    dentro del directorio actual)'''
Mostarinfo(texto2)

texto3='''git clone:
    En el caso de que usted ya haya subido con anterioridad sus archivos a un repositorio o quiere trabajar 
    en el repositorio de alguna otra persona. Tendra que usar el comando git clone
    Este comando nos descargara con todos los datos que tiene el servidor 
    se usa git clone "direccion del repositorio"'''
Mostarinfo(texto3)

print("Bien ahora que ya sabemos como inciar a trabajar con git, vienen una ronda de preguntas\n")
print("Conteste exactamente como pondria el comando en la terminal. Conteste 'pista' si quiere una pista")
print("O 'respuesta' si quiere saber la respuesta, pero recuerde intentar primero por lo menos una vez")
entendio=input("\nDesea continuar? (si o no): ")
os.system("cls") 
inst1='''Primero
    Esta trabajando en un proyecto desarrollado principalmente en lenguaje c, y quiere subir su progreso
    a git. El IDE con el que esta trabajando llena con muchos archivos la carpeta en la que se encuentra
    trabajando para poder compilar y crear el ejecutable. Pero usted solo quiere subir los archivos con 
    extencion .c. ¿Que comando ocuparia?'''
sol1="git add *.c"
pista1="El comando en git a ocupar significa sumar en español y con un asterisco marcamos todos los\n archivos de un mismo tipo"
formpreg(inst1,pista1,sol1)

inst2='''Segundo
    Cual es el comando con el que iniciamos un repositorio en la carpeta en la que estamos trabajando?'''
sol2="git init"
pista2="El comando es como una abreviacion de iniciar"
formpreg(inst2,pista2,sol2)

ints3='''Tercero
    Cual  es el comando que utilizamos para bajar a nuestro equipo un reposiorio almacenado en github?'''
sol3="git clone"
pista3="Se dice clonar reposiorio de github"
formpreg(ints3,pista3,sol3)

ints4='''Cuarto 
    Supongamos que queremos decargar el repositorio https://github.com/daleharvey/pacman 
    que comando ocupariamos?'''
sol4="git clone https://github.com/daleharvey/pacman"
pista4="Es exactamente el mismo comando del problema anterior"
formpreg(ints4,pista4,sol4)

print("Bien ahora que ya sabemos los comando para iniciar a usar git")
print("Veremos comandos que nos ayudaran a guardar los cambio que hagamos que hagamos en el repositorio")
time.sleep(6)
os.system("cls")
   
texto4='''git status:
    Muestra la lista de los archivos que se han cambiado junto con los archivos que están por ser 
    preparados o confirmados.'''
Mostarinfo(texto4)
  
texto5='''git diff:
    Este comando te indica los cambios que has hecho y que todavía no has preparado'''
Mostarinfo(texto5)

texto6='''git comit -m "comentario":
    Crea una confirmacion del estado actual del proyecto. Las confirmaciones se pueden concebir 
    como instantáneas o hitos en el cronograma de un proyecto de Git.
    En pocas palabras el la forma en la que guardamos los cambios de nuestro repositorio local
    con la opcion -m podemos agregar el comentario desde la instruccion
    El comentario puede ayudar a saber los cambios respecto a una confirmacion anterior, por lo que 
    es importante que el comenario haga una referencia a ello
    Por ejemplo supogamos que agregamos archivos CSS para nuestro proyecto, probalemente un buen comentario
    seria "Implementacion CSS", para identificar que apartir de ese commit estaran disponibles esos archivos
    Es importante mencionar que en caso de agregar archivos tendremos que usar el comando add
    para que estos se guarden en el nuevo commit en caso contrario solo se aplicaran los cambios
    a aquellos archivos que fueron agregados con anterioridad.'''
Mostarinfo(texto6)

texto7='''git log:
    Este comando nos permitira ver el hsitorial de confirmaciones hechas en el repositorio'''
Mostarinfo(texto7)

texto8='''git push origin master:
    Este comando permitira subir los cambios a un repositorio remoto siendo master la rama principal
    por default de github (mas adelante se hablaran de las ramas)'''
Mostarinfo(texto8)
print("Segunda ronda de preguntas!!!!")
time.sleep(3)
os.system("cls")



