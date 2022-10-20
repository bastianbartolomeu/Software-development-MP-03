##############################################################
from secrets import choice
from personas import *
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self,nom_rest: str,cocineros:list, repartidores :list,platos :dict ):
        self.nom_rest = nom_rest
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0

    def recibir_pedidos(self,clientes):
        for cliente in clientes:
            platos_preferidos = cliente.plato_preferido
            for plato in platos_preferidos:
                cocinero = self.__energia_cocinero()
                if cocinero:
                    cocinero.cocinar(plato)
                else:
                    pass
            #AHORA HAY QUE OBTENER UN REPARTIDO
            repartidor = self.__energia_repartidor()
            #falta el punto 4,5,6


    def __energia_cocinero(self):
        energia_cocineros = [cocinero.energia for cocinero in self.cocineros]
        cocinero = False
        a = max(energia_cocineros) 
        if  a:
            cocinero = energia_cocineros[energia_cocineros.index(a)]
        
        return cocinero 
    
    def __energia_repartidor(self):
        energia_repartidor = [repartidor.energia for repartidor in self.repartidores]
        cocinero = False
        a = max(energia_repartidor) 
        if  a:
            cocinero = energia_repartidor[energia_repartidor.index(a)]
        
        return cocinero 


        #referencia 
        #energia_cocineros = []
        #for cocinero in self.cocineros : energia_cocineros.append(cocinero.energia)

    
    


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
