"""
Operadores Lógicos
Consigna: Construye un programa que determine si un número ingresado es par y positivo al mismo tiempo.
"""
#Solicitamos al usuario que ingrese un numero

numero= int(input("Ingrese un numero: "))

#Los numeros par se determina con variable % 2 == 0 

if numero > 0 and numero % 2 == 0:
    print ("El numero es positivo y es par")

elif numero < 0 and numero % 2 == 0:
    print ("El numero es negativo y es par")

#Para decir si un numero es distinto de, se hace !=

elif numero > 0 and numero % 2 != 0:
    print ("El numero es positivo pero no es par")

else: 
    print("el numero es negativo y no es par")