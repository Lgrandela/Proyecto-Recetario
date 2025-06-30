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

# Tenemos que darle la bienvenida al usuario e indicarle la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas
# Tambien le va a decir cuantas recetas en total tiene dicha carpeta.
def bienvenida():
    #.glob lo utilizamos para localizar todos los archivos .txt que serían las recetas en sí.
    recetitas = [numero.stem for numero in Path(ruta_principal).glob('**/*.txt')]
    numero_recetas = len(recetitas)
    print("-----------------------------------------------------")
    print('Bienvenido al Recetario. ¿En qué le podemos ayudar?: ')
    print("-----------------------------------------------------")
    print(f'Directorio para llegar a "Recetas", en la cual tenemos un total de {numero_recetas} recetas:\n {ruta_principal}')
    print("-----------------------------------------------------\n")
    print("""
    Por Favor, elija una de las siguientes categorías introduciendo el número que marca dicha categoría:\n
    1. Mostrar y elegir categoría para leer receta.\n
    2. Crear Receta.\n
    3. Crear Categoría.\n
    4. Eliminar receta.\n
    5. Eliminar Categoría.\n
    6. Finalizar aplicación.\n""")

        
'''1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.'''
def elegir_categoria():
    #primero mostramos las categorías que tenemos dentro de la carpeta recetas
    categorias = ruta_principal
    lista_categorias = []    
    for categoria in categorias.iterdir():
        lista_categorias.append(categoria.name)
        print(categoria.name)
    # y seguidamente le pedimos al usuario que elija una de las categorias
    eleccion = input("¿Qué categoría elije?:\t")
    preguntar = True
    contador = 0
    while preguntar == True:
        contador += 1
        if eleccion.capitalize() in lista_categorias:
            preguntar = False
            return eleccion
        elif contador%2 == 0:
            print('\nTambién puede volver al inicio escribiendo "Salir"')
        else:
            print("Por favor, elija una categoría correcta y escríbala tal y como aparece en pantalla.\n")
            for categoria in categorias.iterdir():
                print(categoria.name)
            eleccion = input("¿Qué categoría elije?:\t")
            salida = eleccion.capitalize()
            if salida == 'Salir':
                preguntar = False
                return salida
    
            

def leer_receta(eleccion):
    ruta_recetas = Path(ruta_principal,eleccion)
    # Almacenamos en 'recetas' la iteración de los archivos que se encuentran en la carpeta elegida por el usuario
    recetas = [receta.stem for receta in ruta_recetas.iterdir()]
    #mostramos lar recetas para preguntar cual quiere leer
    print(recetas)
    print(f'\n¿Qué receta quiere leer en concreto?: ')
    elegir = input("(RECUERDO, escriba la receta tal y como aparece en pantalla)\nElija qué receta quiere leer:  ")
    while elegir not in recetas:
        print('Cuando quiera volver al inicio escriba "Salir".')
        print('Por favor, escriba bien la receta')
        print(recetas)
        elegir = input("¿Qué receta quiere leer en concreto?: ")
        if elegir.capitalize() == 'Salir':
            break
    if elegir in recetas:    
        receta = Path(ruta_recetas,(elegir+'.txt'))
        system('cls')
        print(f'Aquí tiene su receta de {elegir}:\n\n{receta.read_text()}\n\n') 
        salir = True
        while salir:
            salida = input('Cuando quiera volver al inicio escriba aquí "Salir".\t').capitalize()
            if salida == 'Salir':
                salir = False
       
'''2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
a crear ese archivo en el lugar correcto.'''
def crear_receta(eleccion):
    #Aqui elegimos la categoría para saber donde creamos la nueva receta (utilizar 'ruta'.with_name())
    ruta_recetas = Path(ruta_principal,eleccion)
    archivo = input('Escriba el nombre de la Receta:    ')
    crear = Path(ruta_recetas,(archivo+'.txt'))
    crear.touch()
    receta = input("Escriba a continuación la Receta completa:\n\n")
    crear.write_text(receta)
    '''3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
una carpeta nueva con ese nombre.'''

def crear_categoria():
    nueva_categoria = input('Escriba el nombre de su nueva categoria:   ')
    nueva_ruta = Path(ruta_principal,nueva_categoria)
    nueva_ruta.mkdir()
    
    
    '''4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
a eliminar'''
def eliminar_receta(eleccion):
    ruta_recetas = Path(ruta_principal,eleccion)
    # Almacenamos en 'recetas' la iteración de los archivos que se encuentran en la carpeta elegida por el usuario
    recetas = [receta.stem for receta in ruta_recetas.iterdir()]
    #mostramos lar recetas para preguntar cual quiere eliminar
    print(recetas)
    eliminar = 'no'
    while eliminar == 'no':
        print('Si no quiere eliminar ninguna receta escriba "Salir".\n')
        print(f'\n¿Qué receta quiere eliminar en concreto?: ')
        elegir = input("(RECUERDO, escriba la receta tal y como aparece en pantalla)\nElija qué receta quiere eliminar:  ")
        if elegir.capitalize() == 'Salir':
            break
        while elegir not in recetas:
                print('Por favor, escriba bien la receta')
                print(recetas)
                elegir = input("¿Qué receta quiere eliminar en concreto?: ")
        receta = Path(ruta_recetas,(elegir+'.txt'))
        eliminar = input(f'¿Está seguro de que quiere eliminar la Receta {elegir}?(si/no):     ')
        if eliminar == 'si':
            system('cls')
            print(f'Ha eliminado {receta}.')
            receta.unlink()
            eliminar = 'si'
        elif eliminar == 'no':
            system('cls')

        
    # print(f'¿Está seguro que quiere eliminar la receta {elegir}?:\n\n{receta.read_text()}\n\n') 
    # Path.unlink(missing_ok=False) esto como idea para eliminar una receta
    '5. La opción 5, le va a preguntar qué categoría quiere eliminar'
def eliminar_categoria():
    categorias = ruta_principal
    lista_categorias = []    
    for categoria in categorias.iterdir():
        lista_categorias.append(categoria.name)
        print(categoria.name)
    eleccion = input('Escriba el nombre de la categoria que quiere eliminar:   ')
    preguntar = True
    while preguntar == True:
        if eleccion.capitalize() in lista_categorias:
            remove_ruta = Path(ruta_principal,eleccion)
            remove_ruta.rmdir()
            preguntar = False
        else:
            print('\nTambién puede volver al inicio escribiendo "Salir"\n')
            print("Por favor, elija una categoría correcta y escríbala tal y como aparece en pantalla.\n")
            for categoria in categorias.iterdir():
                print(categoria.name)
            eleccion = input("¿Qué categoría elije?:\t")            
            salida = eleccion.capitalize()
            if salida == 'Salir':
                break
    
    '6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.'
#esto lo tenemos dentro de la funcion opciones() para que finalice la ejecución del código      
# Vamos a pedir al usuario que elija una de las siguientes opciones:
#Necesitamos el numero como argumento para realizar la selección de opciones
def opciones(num):
    if num == 1:
        eleccion_usuario = elegir_categoria()
        if eleccion_usuario.capitalize() != 'Salir':
            leer_receta(eleccion_usuario)
    elif num == 2:
        eleccion_usuario = elegir_categoria()
        if eleccion_usuario.capitalize() != 'Salir':
            crear_receta(eleccion_usuario)
    elif num == 3:
        crear_categoria()
    elif num == 4:
        eleccion_usuario = elegir_categoria()
        if eleccion_usuario.capitalize() != 'Salir':
            eliminar_receta(eleccion_usuario)
    elif num == 5:
        eliminar_categoria()
    elif num == 6:
        finalizar = False
        print('Que tenga un buen día.')
        return finalizar
        
    else:
        print('Por favor lea bien las opciones y elija una de ellas.')



finalizar = True
while finalizar:
    system('cls')
    bienvenida()
    numero = int(input("¿qué número elije?:  "))
    print("\n")
    resultado = opciones(numero)
    if resultado == False:
        finalizar = resultado