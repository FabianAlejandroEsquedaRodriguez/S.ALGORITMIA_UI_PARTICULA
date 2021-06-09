from particula import Particula
import json
from pprint import pprint, pformat
from queue import PriorityQueue

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

        return str

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

    def recorridoPrim(self, grafo, or_x, or_y):
        listaVisitados = [] #Lista de visitados
        grafoResultante = {} #Grafo resultante
        colaP = PriorityQueue()#Esta es la lista ordenada

        #Elegir un nodo inicial
        nodoInicial = (or_x, or_y)
        #Meter el nodo inicial a la lista de visitados
        listaVisitados.append(nodoInicial)
        
        # colaP.put(nodoInicial)
        if nodoInicial in grafo:
            # #Agregar los adyacentes del nodo incial a la cola de prioridad
            for adyacentes in grafo[nodoInicial]:#Por cada adyacente en el nodo inicial
                orig = nodoInicial
                destino = (adyacentes[0], adyacentes[1])#Toma el destino x,y en la tupla del adyacente
                distancia = (adyacentes[2])#Toma la distancia en el adyacente en la tupla del adyacente
                
                conexion = (orig, destino)#Ver donde se hace el enlace origen -> destino
                arista = (distancia, conexion)#Arista (distancia, (origen, destino))

                colaP.put(arista)

            # #Mientras la cola de prioridad no este vacia
            while not colaP.empty():
                arista = colaP.get()#Para obtener la arista con el menor peso/distancia
                # print("Sale de la cola: ", arista)
                
                distMinima = arista[0]#Distancia minima en la posicion 0 de la tupla (arista)
                x = arista[1]#La tupla en la posicion 1 en la arista (origen, destino)
                origReal = x[0]#Origen
                destReal = x[1]#Destino

                nuevaArista = (destReal, distMinima)
                reciproco = (origReal, distMinima)

                if not destReal in listaVisitados:#Si el destino real no esta en la lista de visitados
                    listaVisitados.append(destReal)#Agregarlo a la lista

                    for adyac in grafo[destReal]:#Por cada adyacente en el grafo
                        origen2 = destReal
                        destino2 = (adyac[0], adyac[1])
                        distancia2 = (adyac[2])
                        
                        conexion2 = (origen2, destino2)#Ver donde se hace el enlace origen -> destino
                        arista2 = (distancia2, conexion2)

                        colaP.put(arista2)

                    if origReal in grafoResultante:
                        grafoResultante[origReal].append(nuevaArista)#Se agrega el valor de la nueva arista a
                                                                    # la key en el grafo resultante
                    else:
                        grafoResultante[origReal] = [nuevaArista]#Se asigna el valor de la nueva arista a la key
                    
                    if destReal in grafoResultante:
                        grafoResultante[destReal].append(reciproco)
                    else:
                        grafoResultante[destReal] = [reciproco]
        else:
            grafo[0] = 0

        return grafoResultante

    def PRIM(self, x, y):
        grafoR = Contenedor_particulas.Diccionario(self)
        prim = Contenedor_particulas.recorridoPrim(self, grafoR, x, y)

        print("\nRecorrido de PRIM\n")
        pprint(prim, width=40, indent=1)

        return prim
            