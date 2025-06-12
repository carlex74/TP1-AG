from funciones import generarPoblacion,ruleta,torneo,decimal,funcionObjetivo,mayorminimo,mutacion, CROSSOVER,fitnes,elite,poblacion_sin_elite,poblacionelite,pasaje_arreglo,graficar_convergencia
import matplotlib.pyplot as plt
import numpy as np
################################################################      OPCION D     ###########################################################################################

def opcionD():
    poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
    acum=0 #Acumula el fitnness
    acumdeci=0
    prom=0
    fit=fitnes(poblacion,10)
    menores=[]#Muestra final 
    mayores=[] #Muestra final 
    promedio=[]#Muestra final 
    mutaciones=[] #Muestra final 
    mutaciones1=[] #Muestra final 
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
        porcentaje=0
        cross=CROSSOVER(padre1,padre2,porcentaje)
        if cross==False:#puede no realizarce crossover
            print("--------------------------")
            print(" NO SE REALIZO CROSSOVER")
            print("--------------------------")
            mayor,menor=mayorminimo(poblacion)
            menores.append(menor)
            mayores.append(mayor)
            promedio.append(prom/10)
            porcentaje=1
            mutacionesp=[]
            mutacionesp,muta1=mutacion(padre1,porcentaje)
            mutacionesp,muta=mutacion(padre2,porcentaje)
            mutaciones.append(muta)
            mutaciones1.append(muta1)

        else:
            print(cross)
            porcentaje=1
            mutacionesp=[]
            mutacionesp,muta1=mutacion(padre1,porcentaje)
            mutacionesp,muta=mutacion(padre2,porcentaje)
            mutaciones.append(muta)
            mutaciones1.append(muta1)
            print("mutacion:",muta, muta1)
            #reemplazamos los padres x los hijos
            for i in range(0,10):
                if padre1==poblacion[i]:
                    poblacion[i]=mutacionesp[0]
                elif padre2==poblacion[i]:
                    poblacion[i]=mutacionesp[1]
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
    decimales_mayores=pasaje_arreglo(mayores)
    decimales_menores=pasaje_arreglo(menores)

    # --- 3. Generar las tres gráficas solicitadas ---

    # Gráfica para 20 iteraciones
    graficar_convergencia(decimales_menores[:20], decimales_mayores[:20], promedio[:20], 'Evolución del Fitness (20 Generaciones)')

    # Gráfica para 100 iteraciones
    graficar_convergencia(decimales_menores[:100], decimales_mayores[:100], promedio[:100], 'Evolución del Fitness (100 Generaciones)')

    # Gráfica para 200 iteraciones
    graficar_convergencia(decimales_menores[:200], decimales_mayores[:200], promedio[:200], 'Evolución del Fitness (200 Generaciones)')

   
    pausa=input()
    op=True
    return op
########################################################################################################################################################decimales_menores[: