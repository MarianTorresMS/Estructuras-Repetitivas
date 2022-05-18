""" Calcular la suma de los N primeros números
naturales"""

suma= 0
i=1
N=int(input("ingrese un numero natural: "))

while (i <= N):
    suma = suma + i
    i = i + 1
print("La suma es:" , suma)