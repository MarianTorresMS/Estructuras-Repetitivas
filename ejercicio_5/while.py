"""Ejercicio No.5 
Programa para que dado un número determinar cuántos dígitos tiene."""

numero=int(input("ingrese el numero: "))
contador=0
while numero>0:
    numero=numero//10
    contador=contador+1

print("El numero ingresado tiene: " +str(contador) + "digitos")