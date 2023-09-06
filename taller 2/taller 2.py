# TALLER 2 PYTHON
# AUTOR(A): Juan Camilo Blandón Henao
# FECHA: 27/06/2023

from datetime import date 
hoy = date.today()         # fecha actual
print("Hoy es el dia: ",hoy)

a=int(input("digite el primer numero: "))
b=int(input("digite el segundo numero: "))
c=int(input("digite el tercer numero: "))
x=[a,b,c]
print("el valor maximo es", max(x))
print("el valor minimo es", min(x))
print("la suma de los tres numeros es: ",sum(x))
print()
z=float(input("digite un numero con decimales: "))
redondeado=round(z)
print("el valor de ", z, "redondeado es: ", redondeado)
print()
frase=input("digite una oracion: ")
print("la frase en mayuscula es: ", frase.upper())
print("la frase en minuscula es: ", frase.lower())
print("la frase en mayuscula inicial es: ", frase.capitalize())
print("la frase con palabras en mayusculas es: ", frase.title())
print("la longitud de la frase es: ", len(frase), "caracteres")
print()
print("FIN")
