

from funciones import generarPoblacion,ruleta,torneo,decimal,funcionObjetivo,mayorminimo,mutacion, CROSSOVER,fitnes,elite,poblacion_sin_elite,poblacionelite
from opcionA import opcionA
from opcionB import opcionB
from opcionC import opcionC
#from rich import print
def menu():
    
    print("--------------BIENVENIDOS AL TP--------- ------------")
    print("             Elija la opcion deseada:                ")
    print("          1-AG ruleta de 20, 100 y 200")
    print("          2-AG torneo de 20, 100 y 200")
    print("          3-AG ruleta elitista")
    print("          4-AG variante propia")
    print("          5-salida")
    print("-----------------------------------------------------")
    op=int(input("opcion:"))
    while op <1 or op>5:    
        op=int(input("opcion:"))
    return op
op=menu()
if op==1:
    opcionA()
if op==2:
    opcionB()
if op==3:
    opcionC()