

from funciones import ruleta,torneo
from AlgoritmoIteraciones import AlgoritmoIteraciones
from AlgoritmoElitismo import AlgElitismo

def menu():
    
    print("--------------BIENVENIDOS AL TP--------- ------------")
    print("             Elija la opcion deseada:                ")
    print("          1-AG ruleta ")
    print("          2-AG torneo ")
    print("          3-AG ruleta elitista")
    print("          4-AG variante propia")
    print("          5-salida")
    print("-----------------------------------------------------")
    op=int(input("opcion:"))
    while op <1 or op>5:    
        op=int(input("opcion:"))
    return op

def main():

    op=menu()

    if op==1:
        AlgoritmoIteraciones(ruleta)
    if op==2:
        AlgoritmoIteraciones(torneo)
    if op==3:
        AlgElitismo(ruleta)
    if op == 4:
        AlgoritmoIteraciones(ruleta, 100)
    if op==5:
        input("Saliendo, presione una tecla para continuar . . .")
    else:
        print("NoSale")
        main()


main()
