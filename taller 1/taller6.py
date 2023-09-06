# TALLER 5 PYTHON
# AUTOR: Juan Camilo Blandon Henao
# FECHA: 15/07/2023

from datetime import date
hoy = date.today()   # fecha actual
print("hoy es el dia: ", hoy)
print()
print("TALLER 6 CICLOS ITERATIVOS CON LA SENTENCIA WHILE")
print()
num1=int(input("digite un número: "))
print("*** ciclo controlado por contador ***")
i = 1
while i<=num1:
    print(i)
    i += 1
print("fin del ciclo")

print()
print("*** ciclo controlado por evento ***")
i = 1
numero1=5
numero2=int(input("digite un número del 1 al 10: "))
while numero1 != numero2:
    i += 1
    numero2=int(input("digite un número del 1 al 10: "))
print("acertaste en el intento numero ", i)
print("fin del ciclo")

print()
print("***ciclo abortado con la sentencia break***")
amistad=input("digite el nombre de una amistad: ")
amistad=amistad.upper()
for character in amistad:
    print(character)
    if character == "A":
        break
print("fin del ciclo")
print()
print("FIN")