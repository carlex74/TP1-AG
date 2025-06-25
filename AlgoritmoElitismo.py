from funciones import limpiar_pantalla,cantidad_iteraciones,generarPoblacion,ruleta,torneo,decimal,mutacion_D,funcionObjetivo,mayorminimo,mutacion, CROSSOVER,fitnes,elite,poblacion_sin_elite,poblacionelite,pasaje_arreglo,graficar_convergencia, ordenarPoblacionSegunFitness
import matplotlib.pyplot as plt
import numpy as np
################################################################      OPCION A      ###########################################################################################

def AlgElitismo(metodoSeleccion, porcentajeMutacion = 0.05):

# =============================================================================
# Declaraciones iniciales
# =============================================================================
    acum=0 #Acumula el fitnness
    acumdeci=0
    porcentajeCrossover=0.75
    #porcentajeMutacion=0.05
    prom=0
    menores=[]#Muestra final 
    mayores=[] #Muestra final 
    promedio=[]#Muestra final 
    mayoresFit=[]
    menoresFit=[]

# =============================================================================
# Poblacion inicial
# =============================================================================

    poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
    fit=fitnes(poblacion,len(poblacion))
    poblacion, fit = ordenarPoblacionSegunFitness(poblacion,fit)
    #Mayores y promedio                
    mayor,menor=poblacion[0],poblacion[len(poblacion)-1]
    menores.append(menor)
    mayores.append(mayor)
    for i in range (len(poblacion)):
        deci=decimal(poblacion[i])
        prom+=funcionObjetivo(deci)
    promedio.append(prom/len(poblacion))

# =============================================================================
# Printeo de poblacion inicial
# =============================================================================

    print("_________________________________________POBLACION INICIAL_________________________________________________________________________")
    print("               arreglo binario                                                              decimal       funcion       fitnes")
    for i in range (0,10):
        deci=decimal(poblacion[i])
        acumdeci+=deci
        print (poblacion[i], deci ,funcionObjetivo(deci),fit[i])
        acum+=fit[i]
        prom+=funcionObjetivo(deci)
    print("___________________________________________________________________________________________________________________________________")

# =============================================================================
# Iteraciones
# =============================================================================

    ciclos=cantidad_iteraciones()

    for t in range(ciclos-1):

        # =============================================================================
        # Seleccion de elites
        # =============================================================================
        fit=fitnes(poblacion,len(poblacion))
        #Ordena la poblacion segun su fitness
        poblacion, fit = ordenarPoblacionSegunFitness(poblacion,fit)
        #Separa los 2 mejores 
        mayorIndiv1, mayorIndiv2 = poblacion[:2]
        mayorFit1, mayorFit2 = fit[:2]
        #Remueve los 2 mejores de la poblacion para hacer el crossover
        poblacion.remove(mayorIndiv1)
        poblacion.remove(mayorIndiv2)
        fit.remove(mayorFit1)
        fit.remove(mayorFit2)


        padres = []

        #Seleccion de padres
        for i in range(int(len(poblacion)/2)): 
            padres.append(((metodoSeleccion(poblacion,fit)),metodoSeleccion(poblacion,fit)))
            """
            #Verificar que no sea el mismo padre
            while padres[i][0] == padres[i][1]: 
                print("Dando vueltas?")
                padres[i] = (padres[i][0],metodoSeleccion(poblacion,fit))
            """


        #Se hace el crossover
        hijos = []
        for i in range(len(padres)):
            potencialesHijos = CROSSOVER(padres[i][0],padres[i][1],porcentajeCrossover)
            if potencialesHijos != False:
                hijos.append(potencialesHijos)
            else:
                #Si no se hace crossover se reemplazan los mismos padres en el array de hijos
                hijos.append((padres[i][0],padres[i][1]))

        for i in range(len(hijos)):
            #Si no hay crossover no hay mutacion
            if hijos[i]!=False:
                hijo0,muta1=mutacion(hijos[i][0],porcentajeMutacion)
                hijo1,muta=mutacion(hijos[i][0],porcentajeMutacion)    
                hijos[i] = (hijo0,hijo1)

            #reemplazamos los padres x los hijos
            poblacion[i] = hijos[i][0]
            poblacion[len(poblacion)-i-1] = hijos[i][1]     

        #Reordenar nueva poblacion
        fit=fitnes(poblacion,len(poblacion))
        #Ordena la poblacion segun su fitness
        poblacion, fit = ordenarPoblacionSegunFitness(poblacion,fit)

        #Volvemos a insertar los mejores individuos
        poblacion.append(mayorIndiv1)
        poblacion.append(mayorIndiv2)
        fit.append(mayorFit1)
        fit.append(mayorFit2)

        #Ordena la poblacion segun su fitness
        poblacion, fit = ordenarPoblacionSegunFitness(poblacion,fit)

        #Calculo promedio poblacion
        prom=0
        for i in range (len(poblacion)):
            deci=decimal(poblacion[i])
            prom+=funcionObjetivo(deci)

        #Mayores y promedio  
        mayor = poblacion[0]
        menor = poblacion[-1]     

        mayorFit = fit[0]
        menorFit = fit[-1]        
        mayoresFit.append(mayorFit)
        menoresFit.append(menorFit)

        menores.append(menor)
        mayores.append(mayor)
        promedio.append(prom/len(poblacion))
    
# =============================================================================
# Tabla final
# =============================================================================    

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 1 a 20 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                        CROMOSOMA CORRESPONDIENTE AL MAXIMO                                                MAYOR                 MENOR                PROMEDIO                         ")
    for i in range (ciclos-1):
        print("        En la iteracion",i+1,"       ",mayores[i],"       ",round(funcionObjetivo(decimal(mayores[i])),3),"         ",round(funcionObjetivo(decimal(menores[i])),3), "        ", round(promedio[i],3))

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 20 a 100 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print (promedio)
    decimales_mayores=pasaje_arreglo(mayores)
    decimales_menores=pasaje_arreglo(menores)

# =============================================================================
# Graficas
# =============================================================================

    # --- 3. Generar las gráficas solicitadas según la cantidad de generaciones (ciclos)---
    graficar_convergencia(decimales_menores[:ciclos], decimales_mayores[:ciclos], promedio[:ciclos], 'Evolución del Fitness (' + str(ciclos) + ' Generaciones)')

   

    input("Presione una tecla . . .")
    op=input("Hacer otra corrida del mismo metodo?(y/n): ")
    if op.lower() == 'y': AlgElitismo(ruleta,porcentajeMutacion)

    return op
########################################################################################################################################################decimales_menores[: