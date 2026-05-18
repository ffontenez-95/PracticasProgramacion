"""
Mayor de tres números 
Situación: Ingresar tres números y mostrar cuál es el 
mayor de los tres. 
"""

num1= int(input("Ingrese el primer numero\n"))
num2= int(input("Ingrese el segundo numero\n"))
num3= int(input("Ingrese el tercer numero\n"))

if num1 > num2 and num1>num3:
    print(f"El primer numero: {num1} es mayor que los otros dos")


elif num2 > num1 and num2>num3:
    print(f"El segundo numero: {num2} es mayor que los otros dos")

else:
    print(f"El tercer numero: {num3} es mayor que los otros dos")

