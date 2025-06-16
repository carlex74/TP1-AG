from funciones import ordenarPoblacionSegunFitness, generarPoblacion, fitnes

pob = generarPoblacion(15,10)
fit = fitnes(pob,len(pob))

print(fit)
print(pob)
print("--------------------------------------------------------------\n\n\n-----------------------------------------------------------")
pob,fit = ordenarPoblacionSegunFitness(pob,fit)

print(fit)
print(pob)
