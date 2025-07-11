import random
import math
import matplotlib.pyplot as plt
import numpy as np
import os

#limpiar pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

#Funcion que determina si es 0 o 1
def detNumero():

    nRandom=round(random.random(),1)
    if nRandom<0.5:
        return 0
    else:
        return 1

# Definicion de la funcion objetivo
def funcionObjetivo(x):

    return (x/((2**30)-1))**2

# funcion para generar la poblacion inicial
def generarPoblacion(numeroIndividuos, tamano):#Tamaño de la cadena binaria
    poblacion = []
    for i in range(numeroIndividuos):
        individuo=[]
        for j in range(tamano):
            individuo.append(detNumero())
        poblacion.append(individuo)
    
    return poblacion

# pasaje de un binario a decimal
def decimal(binario):
    
    decimal=0
    puntero=0
    for i in range (len(binario)):
        decimal = decimal + binario[puntero]*(2**(29-puntero))
        puntero+=1

    return decimal

def fitnes(poblacion, numeroIndividuos):
    """Calcula el fitness de cada individuo en la población.
    Devuelve una lista de fitness normalizada."""

    fitness = []
    poblacion = [pasajeBinarioAFuncionObjetivo(p) for p in poblacion]  # Convertir cada individuo a su valor de función objetivo

    print("Poblacion: ", poblacion)
    #Calcular la suma de los individuos
    sumatoria = sum(poblacion)

    for p in poblacion:
        fitness.append(round(p/sumatoria,3))

    return fitness


# Funcion fitness
def fitnesOld(poblacion, numeroIndividuos):
    
    acum = 0
    fitness = []
    indice = 0

    #Acumula la sumatoria de n individuos
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        acum += funcionObjetivo(x)
        indice += 1

    indice = 0

    #Determina el % de esa sumatoria
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        fit = round((funcionObjetivo(x) / acum)*100,0)
        fitness.append(fit)
        indice += 1

    return fitness 

#fitnes con porcentajes menos de 1
def fitnes_1(poblacion, numeroIndividuos):
    
    acum = 0
    fitness = []
    indice = 0

    #Acumula la sumatoria de n individuos
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        acum += funcionObjetivo(x)
        indice += 1

    indice = 0

    #Determina el % de esa sumatoria
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        fit = round((funcionObjetivo(x) / acum),3)
        fitness.append(fit)
        indice += 1

    return fitness 
#CROSSOVER 
def CROSSOVER(padre1,padre2,porcentaje=int) :
    
    nRandom=round(random.random(),2)
    hijo1=[]
    hijo2=[]
    hijos=[]
    
    nCromosomas=len(padre1)-1

    if nRandom<=porcentaje:                     #posibilidad del crossover 75%
        corte=random.randint(0,nCromosomas)
        for i in range(corte):
            hijo1.append(padre1[i])
            hijo2.append(padre2[i])
        k=corte+1
        for k in range(corte,nCromosomas+1):
            hijo1.append (padre2[k])
            hijo2.append(padre1[k])
        hijos = hijo1,hijo2
        return hijos
    else:  
        crossover=False
        return crossover

#MUTACION 
def mutacion (hijo,porcentaje):
    
    nRandom=round(random.random(),2)
    mutacion=False
    if nRandom<=porcentaje:                               #probabilidad de mutacion 5%
        mutado=random.randint(0,29)
        if hijo[mutado]== 1:
            hijo[mutado]=0
        else:
            hijo[mutado]=1
        mutacion=True
        return hijo , mutacion
    else: return hijo , mutacion

#mutacion para punto D
def mutacion_D (hijo):
    mutado=random.randint(0,29)
    if hijo[mutado]== 1:
        hijo[mutado]=0
    else:
        hijo[mutado]=1
    mutacion=True
    return hijo , mutacion

#ruleta
def ruleta(poblacion, fitnes):
    
    fitnes = [f*100 for f in fitnes]

    eleccion = random.randint(0, int(sum(fitnes)) )  
    ruleta = []

    for i in range(len(fitnes)):                    #las repeticiones es la cant de reps que se encontraran en la ruleta
        repeticiones = int(fitnes[i])  
        ruleta += [i] * repeticiones 
    elegido = ruleta[eleccion % len(ruleta)]  
    return poblacion[elegido]

def mayorminimo(poblacion):
    
    return max(poblacion), min(poblacion)

#torneo
def torneo(poblacion, fitnes):
    eleccion = []
    fitneselec=[]
    while len(eleccion) < 4:
        candidato = random.randint(0, 9)
        if candidato not in eleccion:               #para que no repita seleccionados
            eleccion.append(poblacion[candidato])
            fitneselec.append(fitnes[candidato])
    mejor=eleccion[0]
    mejorfit=fitneselec[0]                          #se comienza poniendo el primero como el mejor
    for i in range (1,4):                           #y luego comienzan a enfrentarse entre si
        if fitneselec[i]>mejorfit:
            mejor=eleccion[i]
            mejorfit=fitneselec[i]
    return mejor

#elitismo
def elite(poblacion,fitnes):                        #elegimos los dos primeros numeros para comparar y luego se comparan entre los otros individualmente
    
    mayor1=poblacion[0]
    mayor2=poblacion[1]
    mayorfit1=fitnes[0]
    mayorfit2=fitnes[1]
    for i in range(2,10):
        if mayorfit1 < fitnes[i]:
            mayor1=poblacion[i]
            mayorfit1=fitnes[i]
        elif mayorfit2 < fitnes[i]:
            mayor2=poblacion[i]
            mayorfit2=fitnes[i]
    return mayor1, mayor2

#poblacion sin elites
def poblacion_sin_elite (poblacion, fitnes, mayor1, mayor2):
    
    poblacionE=[]
    fitnesE=[]
    for i in range (10):
        if poblacion[i]!=mayor1 and poblacion[i]!=mayor2:
            poblacionE.append(poblacion[i])
            fitnesE.append(fitnes[i])
    return poblacionE, fitnesE
            
#poblacion elitista
def poblacionelite(poblacionE,mayor1,mayor2):
    
    pobelite=[]
    for i in range(8):
        pobelite.append(poblacionE[i])
    pobelite.append(mayor1)
    pobelite.append(mayor2)
    return pobelite

#pasaje de binario a funcion objetivo
#se pasa un gen binario a decimal y luego se evalua en la funcion objetivo
def pasajeBinarioAFuncionObjetivo(gen):
    """Convierte un gen binario a decimal y lo evalúa en la función objetivo. Despues lo redondea a 3 decimales.
    Devuelve el valor de la función objetivo."""
    return round(funcionObjetivo(decimal(gen)), 3)

#pasaje de todo un arreglo de binario a decimal y de decimales se evalua en la obj
def pasaje_arreglo(array):
    decimales=[]
    for i in range (len(array)):
        y=round(funcionObjetivo(decimal(array[i])),3)
        decimales.append(y)
    return decimales

#graficas
def graficar_convergencia(minimos, maximos, promedios, titulo_grafica):

        # Crea el eje X, que corresponde al número de generaciones
        generaciones = range(1, len(minimos) + 1)

        # Crea la figura y los ejes para la gráfica
        plt.figure(figsize=(12, 7))

        # Dibuja cada línea (Mínimo, Máximo, Promedio)
        plt.plot(generaciones, maximos, color='g', linestyle='-', marker='o', markersize=4, label='Máximo Fitness')
        plt.plot(generaciones, promedios, color='b', linestyle='-', marker='o', markersize=4, label='Promedio Fitness')
        plt.plot(generaciones, minimos, color='r', linestyle='-', marker='o', markersize=4, label='Mínimo Fitness')

        # Añade Título y etiquetas a los ejes
        plt.title(titulo_grafica, fontsize=16)
        plt.xlabel('Generación', fontsize=12)
        plt.ylabel('Valor de la Función Objetivo (Fitness)', fontsize=12)

        # Añade la leyenda para identificar cada línea
        plt.legend()

        # Añade una cuadrícula para facilitar la lectura
        plt.grid(True)

        # Muestra la gráfica
        plt.show()

#menu de iteraciones de 20, 100 y 200
def cantidad_iteraciones():
    print("-------------------------------------------------------------------")
    iteracion=int(input("ingrese la cantidad de iteraciones deseadas (20, 100 o 200):"))
    print("-------------------------------------------------------------------")
    limpiar_pantalla()
    """
    while iteracion!=20 and iteracion!=100 and iteracion!=200:
        print("-------------eror------------------------------------------")
        iteracion=int(input("ingrese la cantidad de iteraciones deseadas (20, 100 o 200):"))
        print("-------------------------------------------------------------------")
        limpiar_pantalla()
    """
    return iteracion

def ordenarPoblacionSegunFitness(poblacion, fitness):
    # Combina las listas en pares y ordena según el fit (de mayor a menor)
    pares_ordenados = sorted(zip(poblacion, fitness), key=lambda par: par[1], reverse=True)
    
    # Separa las listas ordenadas
    poblacionOrdenada, fitnessOrdenado = zip(*pares_ordenados)
    
    # Convierte los resultados de tuplas a listas
    return list(poblacionOrdenada), list(fitnessOrdenado)

def promedioPoblacion(poblacion):
    prom = 0
    for individuo in poblacion:
        sum = pasajeBinarioAFuncionObjetivo(individuo)
        prom += sum

    return (round(prom / len(poblacion), 3))