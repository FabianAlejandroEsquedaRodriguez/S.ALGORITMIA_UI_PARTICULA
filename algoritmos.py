import math

def distancia_euclidiana(x_1, y_1, x_2, y_2):

    distancia = math.sqrt(pow( (y_1 - x_1), 2) + pow((y_2 - x_2), 2) )

    return distancia
    