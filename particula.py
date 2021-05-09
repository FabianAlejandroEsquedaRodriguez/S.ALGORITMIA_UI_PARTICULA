from algoritmos import distancia_euclidiana

class Particula:
    def __init__(self, id = 0, origen_x = 0, origen_y = 0, destino_x = 0,
                        destino_y = 0, velocidad = 0, red = 0, green = 0, blue = 0, distancia = 0.0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.distancia = distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)

    def __str__(self):#Metodo para convertir objetos a string y poder imprimirlos(Similar a la sobrecarga del operador << en C++)
        return (
            'ID: ' + str(self.__id) + '\n'#Para convertir atributos de tipo int a string
            'ORIGEN X: ' + str(self.__origen_x) + '\n' +
            'ORIGEN Y: ' + str(self.__origen_y) + '\n' +
            'DESTINO X: ' + str(self.__destino_x) + '\n' +
            'DESTINO Y: ' + str(self.__destino_y) + '\n' +
            'VELOCIDAD: ' +str(self.__velocidad) + '\n' +
            'RED: ' + str(self.__red) + '\n' +
            'GREEN: ' + str(self.__green) + '\n' +
            'BLUE: ' + str(self.__blue) + '\n' +
            'DISTANCIA: ' + str(self.distancia) + '\n'
        )

    #Metodos de acceso para acceder a los atributos
    @property
    def id(self):
        return self.__id
    
    @property
    def origen_x(self):
        return self.__origen_x
    
    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y
    
    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue

    
    #Convertir las particulas en un diccionario
    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue
        }
