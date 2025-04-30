import math
import random
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


# pasaje de un binario a decimal
def decimal(binario):
    
    decimal=0
    puntero=0
    for i in range (0,30):
        decimal = decimal + binario[puntero]*(2**(29-puntero))
        puntero+=1

    return decimal



# Funcion fitness
def fitnes(poblacion, numeroIndividuos):
    
    acum = 0
    fitness = []
    indice = 0
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        acum += funcionObjetivo(x)
        indice += 1

    indice = 0
    while indice < numeroIndividuos:
        x = decimal(poblacion[indice])
        fit = round((funcionObjetivo(x) / acum)*100,0)
        fitness.append(fit)
        indice += 1

    return fitness 

#CROSSOVER 
def CROSSOVER(padre1,padre2) :
    
    nRandom=round(random.random(),2)
    hijo1=[]
    hijo2=[]
    hijos=[]
    if nRandom<=0.75:                     #posibilidad del crossover 75%
        corte=random.randint(0,29)
        for i in range(corte):
            hijo1.append(padre1[i])
            hijo2.append(padre2[i])
        k=corte+1
        for k in range(corte,30):
            hijo1.append (padre2[k])
            hijo2.append(padre1[k])
        hijos.append(hijo1)
        hijos.append(hijo2)
        return hijos
    else:  
        crossover=False
        return crossover

#MUTACION 
def mutacion (hijo):
    
    nRandom=round(random.random(),2)
    mutacion=False
    if nRandom<=0.05:                               #probabilidad de mutacion 5%
        mutado=random.randint(0,29)
        if hijo[mutado]== 1:
            hijo[mutado]=0
        else:
            hijo[mutado]=1
        mutacion=True
        return hijo , mutacion
    else: return hijo , mutacion

#ruleta
def ruleta(poblacion, fitnes):
    
    eleccion = random.randint(0, sum(fitnes) - 1)  
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
def poblacionelite(poblacionE,mayor1,menor2):
    
    pobelite=[]
    for i in range(8):
        pobelite.append(poblacionE[i])
    pobelite.append(mayor1)
    pobelite.append(mayor2)
    return pobelite


################################################################      OPCION A      ###########################################################################################
op=menu()
if op==1:
    poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
    acum=0
    acumdeci=0
    prom=0
    fit=fitnes(poblacion,10)
    menores=[]
    mayores=[]
    promedio=[]
    mutaciones=[]
    mutaciones1=[]
    print("_________________________________________POBLACION INICIAL_________________________________________________________________________")
    print("               arreglo binario                                                              decimal       funcion       fitnes")
    for i in range (0,10):
        deci=decimal(poblacion[i])
        acumdeci+=deci
        print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
        acum+=fit[i]
        prom+=funcionObjetivo(deci)
    print("___________________________________________________________________________________________________________________________________")
    mayor,menor=mayorminimo(poblacion)
    menores.append(menor)
    mayores.append(mayor)
    print("El mayor gen es:", mayor)
    print("El menor gen es:", menor)
    print("El promedio de la funcion objetivo es:", prom/10)
    promedio.append(prom/10)
    print("suma de decimales:", acumdeci)
    print(acum)

    for t in range(199):
        padre1=ruleta(poblacion,fit)
        padre2=ruleta(poblacion,fit)
        while padre2 == padre1: #verificamos que el padre no se repita
            padre2=ruleta(poblacion,fit)
        print("los padres elegidos son:")
        print (padre1,padre2)
        cross=CROSSOVER(padre1,padre2)
        if cross==False:#puede no realizarce crossover
            print("--------------------------")
            print(" NO SE REALIZO CROSSOVER")
            print("--------------------------")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            promedio.append(prom/10)
            mutaciones.append(False)
            mutaciones1.append(False)

        else:
            print(cross)
            cross[0],muta1=mutacion(cross[0])
            cross[1],muta=mutacion(cross[1])
            mutaciones.append(muta)
            mutaciones1.append(muta1)
            print("mutacion:",muta, muta1)
            #reemplazamos los padres x los hijos
            for i in range(0,10):
                if padre1==poblacion[i]:
                    poblacion[i]=cross[0]
                if padre2==poblacion[i]:
                    poblacion[i]=cross[1]
            fit=fitnes(poblacion,10)
            acumdeci=0
            prom=0
            print("_________________________________________POBLACION NUEVA_________________________________________________________________________")
            print("               arreglo binario                                                              decimal       funcion       fitnes")
            for i in range (0,10):
                deci=decimal(poblacion[i])
                acumdeci+=deci
                print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
                acum+=fit[i]
                prom+=funcionObjetivo(deci)
            print("___________________________________________________________________________________________________________________________________")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            print("El mayor gen es:", mayor)
            print("El menor gen es:", menor)
            print("El promedio de la funcion objetivo es:", prom/10)
            promedio.append(prom/10)
            print("suma de decimales:", acumdeci)
    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 1 a 20 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO                         MUTACION")
    for i in range (20):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 20 a 100 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO")
    for i in range (20,99):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 100 a 200 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO")
    for i in range (100,199):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    pausa=input()
###############################################################################################################################################################
########################################################       OPCION B           #############################################################################
if op==2:
    poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
    acum=0
    acumdeci=0
    prom=0
    fit=fitnes(poblacion,10)
    menores=[]
    mayores=[]
    promedio=[]
    mutaciones=[]
    mutaciones1=[]
    print("_________________________________________POBLACION INICIAL_________________________________________________________________________")
    print("               arreglo binario                                                              decimal       funcion       fitnes")
    for i in range (0,10):
        deci=decimal(poblacion[i])
        acumdeci+=deci
        print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
        acum+=fit[i]
        prom+=funcionObjetivo(deci)
    print("___________________________________________________________________________________________________________________________________")
    mayor,menor=mayorminimo(poblacion)
    menores.append(menor)
    mayores.append(mayor)
    print("El mayor gen es:", mayor)
    print("El menor gen es:", menor)
    print("El promedio de la funcion objetivo es:", prom/10)
    promedio.append(prom/10)
    print("suma de decimales:", acumdeci)
    print(acum)

    for t in range(199):
        padre1=torneo(poblacion,fit)
        padre2=torneo(poblacion,fit)
        while padre2 == padre1: #verificamos que el padre no se repita
            padre2=torneo(poblacion,fit)
        print("los padres elegidos son:")
        print (padre1,padre2)
        cross=CROSSOVER(padre1,padre2)
        if cross==False:#puede no realizarce crossover
            print("--------------------------")
            print(" NO SE REALIZO CROSSOVER")
            print("--------------------------")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            promedio.append(prom/10)
            mutaciones.append(False)
            mutaciones1.append(False)

        else:
            print(cross)
            cross[0],muta1=mutacion(cross[0])
            cross[1],muta=mutacion(cross[1])
            mutaciones.append(muta)
            mutaciones1.append(muta1)
            print("mutacion:",muta, muta1)
            #reemplazamos los padres x los hijos
            for i in range(0,10):
                if padre1==poblacion[i]:
                    poblacion[i]=cross[0]
                if padre2==poblacion[i]:
                    poblacion[i]=cross[1]
            fit=fitnes(poblacion,10)
            acumdeci=0
            prom=0
            print("_________________________________________POBLACION NUEVA_________________________________________________________________________")
            print("               arreglo binario                                                              decimal       funcion       fitnes")
            for i in range (0,10):
                deci=decimal(poblacion[i])
                acumdeci+=deci
                print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
                acum+=fit[i]
                prom+=funcionObjetivo(deci)
            print("___________________________________________________________________________________________________________________________________")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            print("El mayor gen es:", mayor)
            print("El menor gen es:", menor)
            print("El promedio de la funcion objetivo es:", prom/10)
            promedio.append(prom/10)
            print("suma de decimales:", acumdeci)
    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 1 a 20 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO                         MUTACION")
    for i in range (20):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 20 a 100 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO")
    for i in range (20,99):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 100 a 200 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO")
    for i in range (100,199):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    pausa=input()
    ###############################################################################################################################################################
    #####################################################################     OPCION C        ############################################################################
if op==3:
    poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
    acum=0
    acumdeci=0
    prom=0
    fit=fitnes(poblacion,10)
    menores=[]
    mayores=[]
    promedio=[]
    mutaciones=[]
    mutaciones1=[]
    print("_________________________________________POBLACION INICIAL_________________________________________________________________________")
    print("               arreglo binario                                                              decimal       funcion       fitnes")
    for i in range (0,10):
        deci=decimal(poblacion[i])
        acumdeci+=deci
        print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
        acum+=fit[i]
        prom+=funcionObjetivo(deci)
    print("___________________________________________________________________________________________________________________________________")
    mayor,menor=mayorminimo(poblacion)
    menores.append(menor)
    mayores.append(mayor)
    print("El mayor gen es:", mayor)
    print("El menor gen es:", menor)
    print("El promedio de la funcion objetivo es:", prom/10)
    promedio.append(prom/10)
    print("suma de decimales:", acumdeci)
    print(acum)

    for t in range(199):
        ######CAMBIO A RULETA ELITISTA
        mayor1,mayor2=elite(poblacion,fit)
        poblacionE,fitnesE=poblacion_sin_elite(poblacion,fit,mayor1,mayor2) 
        padre1=ruleta(poblacionE,fitnesE)
        padre2=ruleta(poblacionE,fitnesE)
        while padre2 == padre1: #verificamos que el padre no se repita
            padre2=ruleta(poblacionE,fitnesE)
        #####
        print("los padres elegidos son:")
        print (padre1,padre2)
        cross=CROSSOVER(padre1,padre2)
        if cross==False:#puede no realizarce crossover
            print("--------------------------")
            print(" NO SE REALIZO CROSSOVER")
            print("--------------------------")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            promedio.append(prom/10)
            mutaciones.append(False)
            mutaciones1.append(False)

        else:
            print(cross)
            cross[0],muta1=mutacion(cross[0])
            cross[1],muta=mutacion(cross[1])
            mutaciones.append(muta)
            mutaciones1.append(muta1)
            print("mutacion:",muta, muta1)
            #reemplazamos los padres x los hijos
            for i in range(0,2):
                if padre1==poblacionE[i]:
                    poblacionE[i]=cross[0]
                if padre2==poblacionE[i]:
                    poblacionE[i]=cross[1]
            poblacion=poblacionelite(poblacionE,mayor1,mayor2)
            fit=fitnes(poblacion,10)
            acumdeci=0
            prom=0
            print("_________________________________________POBLACION NUEVA_________________________________________________________________________")
            print("               arreglo binario                                                              decimal       funcion       fitnes")
            for i in range (0,10):
                deci=decimal(poblacion[i])
                acumdeci+=deci
                print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
                acum+=fit[i]
                prom+=funcionObjetivo(deci)
            print("___________________________________________________________________________________________________________________________________")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            print("El mayor gen es:", mayor)
            print("El menor gen es:", menor)
            print("El promedio de la funcion objetivo es:", prom/10)
            promedio.append(prom/10)
            print("suma de decimales:", acumdeci)
    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 1 a 20 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO                         MUTACION")
    for i in range (2):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 20 a 100 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO")
    for i in range (20,99):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 100 a 200 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                     MAYOR                 MENOR                PROMEDIO")
    for i in range (100,199):
        print("        En la iteracion",i+1,"       ",decimal(mayores[i]),"         ",decimal(menores[i]), "        ", promedio[i],"               ",mutaciones[i],mutaciones1[i])

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")