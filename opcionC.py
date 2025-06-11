from funciones import generarPoblacion,ruleta,torneo,decimal,funcionObjetivo,mayorminimo,mutacion, CROSSOVER,fitnes,elite,poblacion_sin_elite,poblacionelite
import matplotlib.pyplot as plt
import numpy as np
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
    
    # --- 1. Simulación de tus datos ---
    # Reemplaza esta sección con tus arreglos reales.
    # Estoy generando datos de ejemplo que simulan la convergencia de un AG.

    def generar_datos_ejemplo(iteraciones):
        """Genera datos falsos para el ejemplo."""
        base = np.linspace(100, 50, iteraciones)
        maximos = base + np.random.rand(iteraciones) * 10
        minimos = base - np.random.rand(iteraciones) * 10
        promedios = base + (np.random.rand(iteraciones) - 0.5) * 5
        return list(minimos), list(maximos), list(promedios)

    # Datos para 20, 100 y 200 iteraciones
    minimos_20, maximos_20, promedios_20 = generar_datos_ejemplo(20)
    minimos_100, maximos_100, promedios_100 = generar_datos_ejemplo(100)
    minimos_200, maximos_200, promedios_200 = generar_datos_ejemplo(200)


    # --- 2. Función para graficar ---
    def graficar_convergencia(minimos, maximos, promedios, titulo_grafica):
        """
        Crea una gráfica de convergencia para los resultados de un algoritmo genético.

        Args:
            minimos (list): Lista con los valores mínimos por generación.
            maximos (list): Lista con los valores máximos por generación.
            promedios (list): Lista con los valores promedio por generación.
            titulo_grafica (str): Título para la gráfica.
        """
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


    # --- 3. Generar las tres gráficas solicitadas ---

    # Gráfica para 20 iteraciones
    graficar_convergencia(minimos_20, maximos_20, promedios_20, 'Evolución del Fitness (20 Generaciones)')

    # Gráfica para 100 iteraciones
    graficar_convergencia(minimos_100, maximos_100, promedios_100, 'Evolución del Fitness (100 Generaciones)')

    # Gráfica para 200 iteraciones
    graficar_convergencia(minimos_200, maximos_200, promedios_200, 'Evolución del Fitness (200 Generaciones)')
