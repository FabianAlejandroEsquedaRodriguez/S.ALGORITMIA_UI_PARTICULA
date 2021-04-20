from particula import Particula
import json

class Contenedor_particulas:
    def __init__(self):
        self.__particulas = [] #Lista para almacenar las particulas

    #Metodos para agregar al final, al inicio y mostrar la lista de particulas
    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)
    
    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)#Se inserta al inicio de la lista
    
    def mostrar(self):
        for particula in self.__particulas:
            print(particula)#Con el __str__ en particula.py, podemos imprimir cada particula dentro de la lista
    
    def __str__(self):#Desde aqui accede a la "sobrecarga" que esta en particula.py, para mostrar los objetos
        return "".join(
            str(particulas) + '\n' for particulas in self.__particulas #Va sacando cada particula de la lista
        )

    def guardar(self, ubicacion):#Es la ubicacion que va a recibir desde nuestra interfaz grafica
        #Abre el archivo en una ubicacion y lo abre en modo de lectura
        with open(ubicacion, 'w') as archivo:
            #lista de diccionarios de tipo particula
            #Cada particula que se saque de la lista de particulas, se va a guardar en la lista, va a tener que llamar al metodo to_dict()
            #Lo que se va a guardar va a ser un conjunto de diccionarios
            lista = [particula.to_dict() for particula in self.__particulas]
            print(lista)

            #Vamos a serializar objetos de tipo particula, para poderlos guardar en un archivo con formato json
            json.dump(lista, archivo, indent=5)#Se manda la lista y el archivo en el que se va a guardar


#Pruebas sin leer datos directamente desde el teclado(Fuera de la clase)

# particula1 = Particula(id=1111, origen_x=2, origen_y=3, destino_x=5, destino_y=7,
#                         velocidad=500, red=4, green=8, blue=12)

# particula2 = Particula(id=2222, origen_x=4, origen_y=6, destino_x=10, destino_y=14,
#                         velocidad=1000, red=8, green=16, blue=24)

# contenedor = Contenedor_particulas()

# contenedor.agregar_final(particula1)
# contenedor.agregar_inicio(particula2)
# contenedor.agregar_final(particula2)

# contenedor.mostrar()
