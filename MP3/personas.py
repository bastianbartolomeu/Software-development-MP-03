##############################################################
from math import factorial
from random import randint, randrange

from numpy import isin
from platos import Comestible, Bebestible, Plato
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self,n):
        self.nombre = n
    
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, n: str, tiempo : int):
        super().__init__(n)
        self.tiempo = tiempo
        self.energia = randint(75,100)
        
    def repartir(self,pedido):
        factor_tamano = 0
        factor_velocidad = 0
        if pedido >= 2:
            factor_tamano = 5
            factor_velocidad = 1.25
        elif pedido >= 3:
            factor_tamano = 15
            factor_velocidad = 0.85
        self.energia -= factor_tamano
        self.tiempo *= factor_velocidad

        return  self.tiempo
### FIN PARTE 2.2 ###



### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, n:str,habilidad : int):
        super().__init__(n)
        self.habilidad = habilidad
        self.energia = randint(50,80) 

    # LA INFORMACION DEL PLATO ES UNA LISTA 
    def cocinar(self,informacion_plato):
        plato = self.clasificacio_plato(informacion_plato)
        if isinstance(plato,Comestible):
            self.energia -= 15
        elif isinstance(plato,Bebestible):
            self.bebestible(plato)
        if plato.dificultad > self.habilidad:
            plato.calidad = plato.calidad*0.7
        else:
            plato.calidad = plato.calidad*1.5
        return plato
        
    def bebestible(self,plato):
        if plato == 'Pequeño':
            self.energia -= 5
        elif plato == 'Mediano':
            self.energia -= 8
        elif plato == 'Grande':
            self.energia -= 10

    def clasificacio_plato(self,informacion_plato):
        nom_plo = informacion_plato[0]
        tipo_plato = informacion_plato[1]
        if tipo_plato == 'Comestible':
            return Comestible(nom_plo)
        elif tipo_plato == 'Bebestible':
            return Bebestible(nom_plo)
    

#INSTANCIAS SOLICITADAS EN EL PUNTO 2.3
       
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, n: str,platos_preferido : list):
        super().__init__(n)
        self.platos_favoritos = platos_preferido

    def recibir_pedido(self,pedido: list,demora: int):
        calificacion_restaurant = 10
        if len(pedido) < len(self.platos_favoritos) or demora >20:
            calificacion_restaurant/2
        for plato in pedido:
            if plato.calidad >= 11:
                calificacion_restaurant += 1.5
            elif plato.calidad <= 8:
                calificacion_restaurant -= 3
            else:
                pass
        return calificacion_restaurant

### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
