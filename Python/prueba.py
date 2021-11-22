import time
import os
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

pregunta1 = input("En pocas palabras que es Git?: ")

if(not ("control de versiones" in pregunta1)):
    print("\nLa respuesta es 'Es un sitema de control de versiones que modela sus datos como un conjunto de instantaneas'")
    time.sleep(5)

os.system("cls")
entendio="no"
while(entendio!="si"):    
    print('''Bien ahora que ya sabemos que es git hablaremos de los principales comandos
    git init:
    Supongamos que esta trabajando en una aplicacion y desea subir sus avances a git para 
    tener disponible su trabajo en cualquier lugar y en todo momento
    Lo primero que tendriamos que hacer es abrir la terminal bash de git desde la
    carpeta donde se encuentra el proyecto y escribir "git init".
    Esto crea un nuevo subdirectorio llamado .git que contiene todos los archivos necesarios 
    del repositorio — un esqueleto de un repositorio Git.''')

    entendio=input("\n\nDesea continuar? (si o no): ")
    os.system("cls")

#os.system("cls")
entendio="no"
while(entendio!="si"):    
    print('''git add:
    Ahora que ya inicio el reposiorio local, necesitamos agregar todos los archivos con los que hemos 
    trabajado hasta ahora para ello ocupamos "git add"
    Supongamos que nuestro proyecto ocupamos scripts de python y entre ellos tenemos uno llamado "Menu.py"
    y lo queremos agregar al repositorio
    Ocupariamos "git add Menu.py"
    Otra opcion es agregar todos los scripts de python con una sola instruccion "git add *.py"
    Asi todos los archivos que se encuentren en la carpeta donde nos estamos se agregaran al reposiorio
    y si tenemos muchos archivos de diferente tipo y ademas en distintos directorios podriamos ocupar:
    "git add ." y se agregaran todos los archivos (tambien los que estan dentro de otros directorios
    dentro del directorio actual)''')

    entendio=input("\nDesea continuar? (si o no): ")
    os.system("cls")