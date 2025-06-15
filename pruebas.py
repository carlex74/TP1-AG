import os
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
print("-------------------------------------------------------------------")
iteracion=int(input("ingrese la cantidad de iteraciones deseadas (20, 100 o 200):"))
print("-------------------------------------------------------------------")
limpiar_pantalla()
while iteracion!=20 and iteracion!=100 and iteracion!=200:
    print("-------------eror------------------------------------------")
    iteracion=int(input("ingrese la cantidad de iteraciones deseadas (20, 100 o 200):"))
    print("-------------------------------------------------------------------")
    limpiar_pantalla()
print (iteracion)
input()
