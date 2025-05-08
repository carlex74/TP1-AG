from funciones import generarPoblacion,ruleta,torneo,decimal,funcionObjetivo,mayorminimo,mutacion, CROSSOVER,fitnes,elite,poblacion_sin_elite,poblacionelite

#####################################################################     OPCION C        ############################################################################
def opcionC():
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
    for i in range (19):
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