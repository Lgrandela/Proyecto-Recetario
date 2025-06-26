from pathlib import Path
from os import system
#para utilizar o comprobar la dirección raiz se usa Path.home()
'''Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
estas opciones que tenemos aquí:
'''
#*******************************************************************************************************#
'USAREMOS ESTA RUTA COMO PRINCIPAL QUE ES LA CARPETA "Recetas" DONDE SE ENCUENTRAN LAS CATEGORIAS'
ruta_principal = Path(Path.home(),'Proyecto-Recetario','Recetas')
recetitas = [numero.stem for numero in Path(ruta_principal).glob('**/*.txt')]
numero_recetas = len(recetitas)
# Tenemos que darle la bienvenida al usuario e indicarle la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas
# Tambien le va a decir cuantas recetas en total tiene dicha carpeta.
def bienvenida():
    print("-----------------------------------------------------")
    print('Bienvenido al Recetario. ¿En qué le podemos ayudar?: ')
    print("-----------------------------------------------------")
    print(f'Directorio para llegar a "Recetas", en la cual tenemos un total de {numero_recetas} recetas:\n {ruta_principal}')
    print("-----------------------------------------------------\n")

        
'''1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.'''
def mostrar_categorias():
    #primero mostramos las categorías que tenemos dentro de la carpeta recetas
    categorias = ruta_principal
    lista_categorias = []    
    for categoria in categorias.iterdir():
        lista_categorias.append(categoria.name)
        # print(categoria.name)
    print(lista_categorias)
    return lista_categorias
    
def elegir_categoria():
    eleccion = input("¿Qué categoría elije?: ")
    if eleccion.capitalize() not in mostrar_categorias():
        print("Por favor, elija una categoría correcta y escríbala tal y como aparece en pantalla.")
    else:
        return eleccion
    


def leer_receta(eleccion):
    ruta_recetas = Path(ruta_principal,eleccion)
    # Almacenamos en 'recetas' la iteración de los archivos que se encuentran en la carpeta elegida por el usuario
    recetas = [receta.stem for receta in ruta_recetas.iterdir()]
    #mostramos lar recetas para preguntar cual quiere leer
    print(recetas)
    print(f'\n¿Qué receta quiere leer en concreto?: ')
    elegir = input("(RECUERDO, escriba la receta tal y como aparece en pantalla)\nElija qué receta quiere leer:  ")
    if elegir not in recetas:
        print('Por favor, escriba bien la receta')
    else:
        receta = Path(ruta_recetas,(elegir+'.txt'))
        # system('cls')
        print(f'Aquí tiene su receta de {elegir}:\n\n{receta.read_text()}\n\n') 
        
        
'''2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.'''


def crear_receta():
    #Aqui elegimos la categoría para saber donde creamos la nueva receta (utilizar 'ruta'.with_name())

    '''3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.'''

def crear_categoria(categoria):
    
    
    
    '''4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar'''
def eliminar_receta():
    
    '5. La opción 5, le va a preguntar qué categoría quiere eliminar'
def eliminar_categoria():
    '6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.'
#esto lo tenemos dentro de la funcion opciones() para que finalice la ejecución del código   
    
# Vamos a pedir al usuario que elija una de las siguientes opciones:
#Necesitamos el numero como argumento para realizar la selección de opciones
def opciones(num):
    if num == 1:
        mostrar_categorias()
        # elegir_categoria()
        eleccion_usuario = elegir_categoria()
        leer_receta(eleccion_usuario)
    elif num == 2:
        crear_receta()
    elif num == 3:
        crear_categoria()
    elif num == 4:
        eliminar_receta()
    elif num == 5:
        eliminar_categoria()
    elif num == 6:
        print('Que tenga un buen día.')
        finalizar = True
    else:
        print('Por favor lea bien las opciones y elija una de ellas.')



bienvenida()
finalizar = False
while finalizar != True:
    
    print("""
        Por Favor, elija una de las siguientes categorías introduciendo el número que marca dicha categoría:\n
        1. Mostrar y elegir categoría para leer receta.\n
        2. Crear Receta.\n
        3. Crear Categoría.\n
        4. Eliminar receta.\n
        5. Eliminar Categoría.\n
        6. Finalizar aplicación.\n""")
    numero = int(input("¿qué número elije?:  "))
    print("\n")
    opciones(numero)