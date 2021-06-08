from particula import Particula
import json
from pprint import pprint, pformat

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
    
    #Metodo para hacer una clase iterable y que vaya retornando elementos
    def __iter__(self):
        self.cont = 0#Iicializar el acceso a la lista de particulas

        return self#Retorna la clase o el objeto
    
    #Metodo que retorna lo que hay en la siguiente posicion
    def __next__(self):
        if self.cont < len(self.__particulas):#Si el cont es menos al tamaño de la lista de particulas
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration#lanzar una exepcion

    def __len__(self):#Retorna la longitud de la lista de particulas
        return len(self.__particulas)

    def guardar(self, ubicacion):#Es la ubicacion que va a recibir desde nuestra interfaz grafica
        try:#Valida si es posible crear un archivo
            #Abre el archivo en una ubicacion y lo abre en modo de lectura
            with open(ubicacion, 'w') as archivo:
                #lista de diccionarios de tipo particula
                #Cada particula que se saque de la lista de particulas, se va a guardar en la lista, va a tener que llamar al metodo to_dict()
                #Lo que se va a guardar va a ser un conjunto de diccionarios
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)

                #Vamos a serializar objetos de tipo particula, para poderlos guardar en un archivo con formato json
                json.dump(lista, archivo, indent=5)#Se manda la lista y el archivo en el que se va a guardar

                return 1#Si se pudo hacer
        except:
            return 0#Hubo un error al ejecutar el with open()

    def abrir(self, ubicacion):
        try:
            #Se abre el archivo en modo de lectura, en la ubicacion recibida
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)#Leer archivos json y devolvernos la informacion, en una lista de diccionarios
                
                #Cada diccionario se tiene que ir convirtiendo a una particula
                self.__particulas = [Particula(**particula)for particula in lista]#Borra las particulas que ya tiene para cargar los del archivo
                                                                                #Crear una Particula, usando la informacion que tiene cada particula
                                                #Con los dos asteriscos, le decimos que a las llaves y valores en el .json, los convierta a parametros de la 
                                                #clase particula
            return 1
        except:
            return 0

    #En cada metodo se vuelven a convertir a enteros y flotantes para que haga bien la comparacion 
    def ordenar_ID(self):#Sirve para ordenar las particulas en orden ascendente (ID)
        self.__particulas.sort(key=lambda particulas:int(particulas.id))

    def ordenar_DISTANCIA(self):#Sirve para ordenar las particulas en orden descendente (Distancia)
        self.__particulas.sort(key=lambda particulas:float(particulas.distancia), reverse=True)

    def ordenar_VELOCIDAD(self):#Sirve para ordenar las particulas en orden ascendente (Velocidad)
        self.__particulas.sort(key= lambda particulas:int(particulas.velocidad))

    #Metodo para dibujar el grafo
    def Diccionario(self):
        grafo = dict()

        for particula in self.__particulas:
            # grafo[(particula.origen_x, particula.origen_y)] = [(particula.destino_x, particula.destino_y, int(particula.distancia))]
            # grafo[(particula.destino_x, particula.destino_y)] = [(particula.origen_x, particula.origen_y, int(particula.distancia))]

            arista_origen = (particula.destino_x, particula.destino_y, int(particula.distancia))
            arista_destino = (particula.origen_x, particula.origen_y, int(particula.distancia))

            key_origen = (particula.origen_x, particula.origen_y)
            key_destino = (particula.destino_x, particula.destino_y)

            if key_origen in grafo:
                grafo[(particula.origen_x, particula.origen_y)].append(arista_origen)
            else:
                grafo[(particula.origen_x, particula.origen_y)] = [arista_origen]
            
            if key_destino in grafo:
                grafo[(particula.destino_x, particula.destino_y)].append(arista_destino)
            else:
                grafo[(particula.destino_x, particula.destino_y)] = [arista_destino]
        
        
        str = pformat(grafo, width=40, indent=1)
        print(str)

        return grafo

    #Metodo para poder hacer el recorrido para los grafos
    def DiccionarioRecorridos(self):
        grafo = dict()

        for particula in self.__particulas:

            arista_origen = (particula.destino_x, particula.destino_y)
            arista_destino = (particula.origen_x, particula.origen_y)

            key_origen = (particula.origen_x, particula.origen_y)
            key_destino = (particula.destino_x, particula.destino_y)

            if key_origen in grafo:
                grafo[(particula.origen_x, particula.origen_y)].append(arista_origen)
            else:
                grafo[(particula.origen_x, particula.origen_y)] = [arista_origen]

            if key_destino in grafo:
                grafo[(particula.destino_x, particula.destino_y)].append(arista_destino)
            else:
                grafo[(particula.destino_x, particula.destino_y)] = [arista_destino]


        return grafo

    #Metodo para realizar el recorrido por profundidad en el grafo
    def RecorreProfundidad(self, grafo, x, y):
        visitados = []
        pila = []
        recorrridoProfundidad = []

        key = (x, y)

        if (key in grafo):
            visitados.append(key)
            pila.append(key)

            while (len(pila) > 0):
                vertice = pila[-1]#Acceder al tope de la pila
                recorrridoProfundidad.append(vertice)
                pila.pop()

                for ady in grafo[vertice]:#Por cada adyacente en el vertice
                    if not ady in visitados:
                        visitados.append(ady)
                        pila.append(ady)

        return recorrridoProfundidad
                
    #Metodo para realizar el recorrido por amplitud en el grafo
    def RecorreAmplitud(self, grafo, x, y):

        visitados = []
        cola = []
        recorrridoAmplitud = []

        key = (x, y)

        if (key in grafo):
            visitados.append(key)
            cola.append(key)   

            while (len(cola) > 0):
                vertice = cola[0]#Acceder al inicio de la cola
                recorrridoAmplitud.append(vertice)
                del cola[0]#Desencolar

                for ady in grafo[vertice]:#Por cada adyacente en el vertice
                    if not ady in visitados:
                        visitados.append(ady)
                        cola.append(ady)

        return recorrridoAmplitud

    def recorridoP(self, o_x, o_y):
        recorrerGrafo = Contenedor_particulas.DiccionarioRecorridos(self)
        recorridoP = Contenedor_particulas.RecorreProfundidad(self, recorrerGrafo, o_x, o_y)

        print("Recorrido en Profundidad: ")
        str = pformat(recorridoP, width=35, indent=1)
        print(str)

        return str

    def recorridoA(self, o_x, o_y):
        recorrerGrafo = Contenedor_particulas.DiccionarioRecorridos(self)
        recorridoA = Contenedor_particulas.RecorreAmplitud(self, recorrerGrafo, o_x, o_y)

        print("Recorrido en Profundidad: ")
        str = pformat(recorridoA, width=35, indent=1)
        print(str)

        return str
