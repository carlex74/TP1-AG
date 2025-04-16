import math
import random

def detNumero():

    nRandom=round(random.random(),1)
    if nRandom<0.5:
        return 0
    else:
        return 1

# Definicion de la funcion objetivo
def funcionObjetivo(x):

    return (x/(2**30)-1)**2

# funcion para generar la poblacion inicial
def generarPoblacion(numeroIndividuos, tamano):#Tamaño de la cadena binaria
    poblacion = []

    for i in range(numeroIndividuos):
        individuo=[]
        for j in range(tamano):
            individuo.append(detNumero())
        poblacion.append(individuo)
    
    return poblacion


poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
