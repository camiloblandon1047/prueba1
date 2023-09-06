# TALLER 3 PYTHON
# AUTOR: Juan Camilo Blandon Henao
# FECHA: 11/07/2023

from datetime import date
hoy = date.today()   # fecha actual
print("Hoy es el dia: ", hoy)

a=int(input("digite el valor de A: "))
b=int(input("digite el valor de B: "))
if a>=b:
    print("A es mayor o igual a B")
else:
    print("A es mayor que B")
print()
curso1="requerimientos"
curso2="algoritmos"
print("el curso 1 es: ", curso1)
print("el curso 2 es: ", curso2)
if curso1 == "requerimientos" and curso2 == "algoritmos":
    print("usted estudia programación de software")
else:
    print("usted estudia otro programa diferente a programación de software")
print()
print("***   final de análisis del programa de formación SENA   ***")
print()
frase=input("digite una oración: ")
print("la frase en mayuscula es: ",frase.upper())
longitud=len(frase)
print("la longitud de la frase es: ", longitud, "caracteres")
if longitud>10:
    print("la frase contiene mas de 10 caracteres")
else:
    print("la frase contiene 10 o menos de 10 caracteres")
print()
print("FIN")