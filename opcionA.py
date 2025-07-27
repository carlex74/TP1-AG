from funciones import limpiar_pantalla,cantidad_iteraciones,generarPoblacion,ruleta,torneo,decimal,mutacion_D,funcionObjetivo,mayorminimo,mutacion, CROSSOVER,fitnes,elite,poblacion_sin_elite,poblacionelite,pasaje_arreglo,graficar_convergencia, ordenarPoblacionSegunFitness
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
################################################################      OPCION A      ###########################################################################################

def opcionA(metodoSeleccion, porcentajeMutacion = 0.05):
    df=pd.DataFrame(columns=['Iteracion', 'Mayor', 'Menor', 'Promedio'])

# =============================================================================
# Declaraciones iniciales
# =============================================================================

    poblacion=generarPoblacion(numeroIndividuos=10,tamano=30)
    acum=0 #Acumula el fitnness
    acumdeci=0
    porcentajeCrossover=0.75
    #porcentajeMutacion=0.05
    prom=0
    fit=fitnes(poblacion,10)
    menores=[]#Muestra final 
    mayores=[] #Muestra final 
    promedio=[]#Muestra final 
    mutaciones=[] #Muestra final, lista bool de si hubo o no mutacion (Obsoleto)
    mutaciones1=[] #Muestra final, lista bool de si hubo o no mutacion (Obsoleto)

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
        fit=fitnes(poblacion,len(poblacion))

        #Ordena la poblacion segun su fitness
        poblacion, fit = ordenarPoblacionSegunFitness(poblacion,fit)

        #Seleccion de padres
        padre1=metodoSeleccion(poblacion,fit)
        padre2=metodoSeleccion(poblacion,fit)

        #verificamos que el padre no se repita
        while padre2 == padre1: 
            padre2=metodoSeleccion(poblacion,fit)
        
        
        cross=CROSSOVER(padre1,padre2,porcentajeCrossover)

        #puede no realizarse crossover
        if cross==False:
            
            mutaciones.append(False)
            mutaciones1.append(False)

        #Se realizo crossover
        else:
            
            cross[0],muta1=mutacion(cross[0],porcentajeMutacion)
            cross[1],muta=mutacion(cross[1],porcentajeMutacion)
            mutaciones.append(muta) #Los bool de mutaciones ya no son requeridos pero igual los dejo
            mutaciones1.append(muta1)

            #reemplazamos los padres x los hijos
            for i in range(0,10):
                if padre1==poblacion[i]:
                    poblacion[i]=cross[0]
                elif padre2==poblacion[i]:
                    poblacion[i]=cross[1]


            #Calculo de promedio
            acumdeci=0
            prom=0
            for i in range (0,10):
                deci=decimal(poblacion[i])
                prom+=funcionObjetivo(deci)

                acumdeci+=deci #Estos dos creo q no hacen nada, pero no estoy seguro
                acum+=fit[i]

        #Mayores y promedio                
        mayor,menor=poblacion[0],poblacion[len(poblacion)-1]
        menores.append(menor)
        mayores.append(mayor)
        promedio.append(prom/10)
    
# =============================================================================
# Tabla final
# =============================================================================    

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 1 a 20 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print("                                        CROMOSOMA CORRESPONDIENTE AL MAXIMO                                                MAYOR                 MENOR                PROMEDIO                         ")
    for i in range (ciclos-1):
        print("        En la iteracion",i+1,"       ",mayores[i],"       ",round(funcionObjetivo(decimal(mayores[i])),3),"         ",round(funcionObjetivo(decimal(menores[i])),3), "        ", round(promedio[i],3))
        
        df.loc[i] = [i+1, decimal(mayores[i]), decimal(menores[i]), promedio[i]]

    print("_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_TABLA FINAL 20 a 100 _*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_")
    print (promedio)
    decimales_mayores=pasaje_arreglo(mayores)
    decimales_menores=pasaje_arreglo(menores)

# =============================================================================
# Graficas
# =============================================================================
    df.to_csv(f'./tablas/resultados_cilco:{ciclos}.csv', index=False)

    # --- 3. Generar las gráficas solicitadas según la cantidad de generaciones (ciclos)---
    graficar_convergencia(decimales_menores[:ciclos], decimales_mayores[:ciclos], promedio[:ciclos], 'Evolución del Fitness (' + str(ciclos) + ' Generaciones)')


    input("Presione una tecla . . .")
    op=input("Hacer otra corrida del mismo metodo?(y/n): ")
    if op.lower() == 'y': opcionA(ruleta,porcentajeMutacion)

    return op
########################################################################################################################################################decimales_menores[: