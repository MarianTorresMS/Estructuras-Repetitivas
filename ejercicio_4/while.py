"""Ejercicio No.4 
Programa para obtener la cantidad de los primeros N números
múltiplos de 5."""

a=int(input("Digite el valor de a: "))
b=int(input("Digite el valor de b: "))

if 1<a:
    cont_num=0
    a=a+1
    while(a<=b):
        r= a%5
        if r==0:
            cont_num=cont_num+1
        a=a+1
    print("La cantidad de numero es:" , cont_num)
else:
    print("a debe ser mayor que 1 ")
