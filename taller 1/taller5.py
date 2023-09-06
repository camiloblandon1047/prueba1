# TALLER 5 PYTHON
# AUTOR: Juan Camilo Blandon Henao
# FECHA: 15/07/2023

from datetime import date
hoy = date.today()   # fecha actual
print("hoy es el dia: ", hoy)
print()
print("TALLER 5 CICLOS ITERATIVOS CON LA SENTENCIA FOR")
print()
num1=int(input("digite el primer número: "))
num2=int(input("digite el segundo número (mayor): "))
print("ciclo para el primer número")
for i in range(num1):
    print(i)
print("fin del ciclo")

print()
print("ciclo desde el primer número hasta el segundo número")
for i in range(num1,num2):
    print(i)
print("fin del ciclo")

print()
print("ciclo desde el primer número hasta el segundo número con incremento de 2")
for i in range(num1,num2,2):
    print(i)
print("fin del ciclo")

print()
empresa=input("digite el nombre de una empresa: ")
empresa=empresa.lower()
for character in empresa:
    print(character)
print("fin del ciclo")

print()
print("FIN")