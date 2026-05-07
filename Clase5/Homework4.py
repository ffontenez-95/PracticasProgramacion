"""
Break
programa que pida numeros al usuario hasta que ponga un negativo
"""

while True:
    numero=int(input("Ingrese un numero: \n"))

    if numero < 0: 
        break

print ("Programa finalizado")