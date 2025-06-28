from funciones import ordenarPoblacionSegunFitness, generarPoblacion, fitnes, fitnessV2, pasajeBinarioAFuncionObjetivo

nroIndiv = int(input("Ingrese el numero de individuos: "))
op = 's'
while op == 's':


    pob = generarPoblacion(nroIndiv,10)
    fit = fitnessV2(pob)

    print(fit)
    print(pob)
    print("--------------------------------------------------------------\n\n\n-----------------------------------------------------------")
    pob,fit = ordenarPoblacionSegunFitness(pob,fit)

    print(fit)
    print(pob)

    op = input("Desea continuar? (s/n): ")



# =============================================================================
# Chequeo error de mayores
# =============================================================================
"""
if(menor > mayor):
    print("Error, el menor es mayor que el mayor")
    print("mayores: ",mayores)
    print("\nmenores: ",menores)
    print("\npromedio: ",promedio)
    print("\nmayoresFit: ",mayoresFit)
    print("\nmenoresFit: ",menoresFit)

    print("\npoblacion: ", [pasajeBinarioAFuncionObjetivo(p) for p in poblacion])
    print("\nfit: ", fit)

    input("Presione una tecla para continuar . . .")


if(menor > promedioPoblacion(poblacion)):
    print("Error, el menor es mayor que el promedio")
    print("\nmayores: ",mayores)
    print("\nmenores: ",menores)
    print("\npromedio: ",promedio[t])
    print("\nmayoresFit: ",mayoresFit)
    print("\nmenoresFit: ",menoresFit)

    print("\npoblacion: ", [pasajeBinarioAFuncionObjetivo(p) for p in poblacion])
    print("\nfit: ", fit)

    input("Presione una tecla para continuar . . .")
"""