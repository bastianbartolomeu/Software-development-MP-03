##############################################################
from random import randint, choice
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 1.1 ###
class Plato:
    def __init__(self,n):
        self.nombre = n
        self.calidad = 0
        
### FIN PARTE 1.1 ###

### INICIO PARTE 1.2 ###
class Bebestible(Plato):
    def __init__(self, n):
        super().__init__(n)
        self.tamano = choice(['Pequeño','Mediano','Grande',])
        self.dificultad = self.dificultad_tamano(self.tamano)
        self.calidad = randint(3,8) 
    
    def dificultad_tamano(self):
        difcultad = 0
        if self.tamano == 'Pequeño':
            difcultad = 3
        elif self.tamano == 'Mediano':
            difcultad = 6
        else:
            difcultad = 9
        return difcultad
    
### FIN PARTE 1.2 ###

### INICIO PARTE 1.3 ###
class Comestible(Plato):
    def __init__(self, n):
        super().__init__(n)
        self.dificultad = randint(1,10)
        self.calidad = randint(5,10)

    def dif_plato(self):
        return self.dificultad
    
    def cal_plato(self):
        return self.calidad


    
### FIN PARTE 1.3 ###

if __name__ == "__main__":
    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        un_bebestible = Bebestible("Coca-Cola")
        un_comestible = Comestible("Sopa")
        print(f"Esto es una {un_bebestible.nombre} de tamaño {un_bebestible.tamano} y calidad {un_bebestible.calidad}.")
        print(f"Esto es una {un_comestible.nombre} de dificultad {un_comestible.dificultad} y calidad {un_comestible.calidad}.")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
