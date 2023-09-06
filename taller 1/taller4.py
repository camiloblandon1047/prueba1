# TALLER 4 PYTHON
# AUTOR: Juan Camilo Blandon Henao
# FECHA: 11/07/2023

from datetime import date
hoy = date.today()   # fecha actual
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE LAS CLASES DE TRIANGULOS")
a=int(input("digite el valor de A: "))
b=int(input("digite el valor de B: "))
c=int(input("digite el valor de C: "))

if a==b and a==c and b==c:
    print("EL TRIANGULO ES UN EQUILATERO")
else:
    if a==b or b==c or a==c:
        print("EL TRIANGULO ES ISOCELES")
    else:
        print("EL TRIANGULO ES ESCALENO")
print()
animal = input("digite un animal: ")
animal = animal.upper()
if animal=="PERRO":
    print("este animal es el mejor amigo del hombre: ", animal)
elif animal=="GATO":
    print("este animal persigue a los ratones: ", animal)
elif animal=="OSO":
    print("este animal vive en el polo norte: ", animal)
else: 
    print("no es PERRO, no es GATO, ni es OSO... es: ", animal)
print()
print("FIN")