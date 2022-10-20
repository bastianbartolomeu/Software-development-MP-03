##############################################################
from sklearn.svm import l1_min_c
from personas import *
from random import seed
import random

from restaurante import Restaurante
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###

def crear_repartidores():
    lista = ['Juan','Claudio']
    r1 = Repartidor(lista[0],randint(20,30))
    r2 = Repartidor(lista[1],randint(20,30))
    lista_repartidores = [r1,r2]
    return lista_repartidores

def crear_cocineros():
    lista = ['Patricio','Estefania','Andrea','Miguel','Ignacia']
    c1 = Cocinero(lista[0],randint(1,10))
    c2 = Cocinero(lista[0],randint(1,10))
    c3 = Cocinero(lista[0],randint(1,10))
    c4 = Cocinero(lista[0],randint(1,10))
    c5 = Cocinero(lista[0],randint(1,10)) 
    # habilidad 1 a 10
    lista_cocineros = [c1,c2,c3,c4,c5]
    return lista_cocineros

def crear_clientes():
    # entre 1 a 5 platos 
    # 5 clientes
    lista_platos = ['Cazuela','Caldillo de congrio','Curanto','Carbonada','Cazuela nogada',
    'Chancho en piedra','Chorrillana','Choriqueso','Empanada de pino','Pastel de jaiba',
    'Sopaipillas','Machas a la parmesana','Milcao','Pastel de choclo','Porotos granados',
    'Chupes','Pollo al barro','Plateada','Locos','Humitas','Ensalada a la chilena','Chumbeque','Empolvados',
    'Calzones rotos','Leche asada','Picarones','Melvin','Piscola','Cola de mono']
    
    cl1 = Cliente('Pdro Pablo',random.sample(lista_platos,4))
    cl2 = Cliente('Miguel Acuña',random.sample(lista_platos,5))
    cl3 = Cliente('Paulina Mendoza',random.sample(lista_platos,5))
    cl4 = Cliente('Francisca Muñoz',random.sample(lista_platos,5))
    cl5 = Cliente('Catalina Ortega',random.sample(lista_platos,5))

    lista_clientes =[cl1,cl2,cl3,cl4,cl5]
    return lista_clientes

def crear_restaurante():
    dicionario_platos = {'Cazuela':'Comestible','Caldillo de congrio':'Comestible','Curanto':'Comestible',
    'Carbonada':'Comestible','Cazuela nogada':'Comestible','Chancho en piedra':'Comestible',
    'Chorrillana':'Comestible','Choriqueso':'Comestible','Empanada de pino':'Comestible',
    'Pastel de jaiba':'Comestible','Sopaipillas':'Comestible','Machas a la parmesana':'Comestible',
    'Milcao':'Comestible','Pastel de choclo':'Comestible','Porotos granados':'Comestible',
    'Chupes':'Comestible','Pollo al barro':'Comestible','Plateada':'Comestible','Locos':'Comestible',
    'Humitas':'Comestible','Ensalada a la chilena':'Comestible','Chumbeque':'Comestible',
    'Empolvados':'Comestible','Calzones rotos':'Comestible','Leche asada':'Comestible','Picarones':'Comestible',
    'Melvin':'Bebestible','Piscola':'Bebestible','Cola de mono':'Bebestible','Chicha dulce':'Bebestible',
    'Chicha fuerte':'Bebestible', 'Cerveza artesanal':'Bebestible'}
    
    lista_cocineros = ['Patricio','Estefania','Andrea','Miguel','Ignacia']
    nombre_restaurant = 'Típicos Chilenos'
    lista_repartidor = ['Juan','Claudio','Claudia','Marcela','Angel']


    cocinero = crear_cocineros()
    repartidor = crear_repartidores()
    restaurant = Restaurante(nombre_restaurant,lista_cocineros,lista_repartidor,dicionario_platos)
    return restaurant

    

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("With Love")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
