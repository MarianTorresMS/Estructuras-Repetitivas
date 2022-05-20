"""Ejercicio No.3 
Programa para Dado un rango de números enteros obtener la
cantidad de números pares que contiene."""
a=int(input("Digite el valor de a: "))
b=int(input("Digite el valor de b: "))

if (a<b):
    cont_num=0
    a=a+1
    while (a<b):
        r=a%2
        if (r==0):
             cont_num=cont_num+1
        a=a+1
    print("La cantidad de numeros es: ", cont_num)
else:
    print("a debe ser menor que b")