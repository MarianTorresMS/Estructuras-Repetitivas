"""Eercicio No. 2
Programa que dado un rango de numeros enteros obtener la cantidad de numeros que contiene"""
c=0

print("ingrese el primer numero del rango: ")
xi=int(input())
print(("Ingrese el ultimo numero del rango: "))
xf=int(input())

c=0
i=xi+1
if xi<xf:
    while i<xf:
        i=i+1
        
        c=c+1
        print(xi+c)
else:
    print ("el xi debe ser menor del xf")
    print("La cantidad de numeros es: " + str(c))