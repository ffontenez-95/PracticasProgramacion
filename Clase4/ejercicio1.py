"""
Cine:
Un cine ofrece descuento del 50% a menores de 12 años y a jubilados mayores de 65. 
Consigna: Pedir la edad y mostrar si paga entrada completa o con descuento.
"""

print ("--- BIENVENIDO AL CINE ---")

#Pedimos la edad al cliente
edad=int(input("¿Que edad tenes?"))

#Aplicamos reglas para determinar si tiene que tener descuento o no, en base a la edad:

if edad > 65:
    print ("Tenes beneficio del 50% de descuento")

elif edad<12:
    print ("Tenes beneficio del 50% de descuento")

else: 
    print ("No tenes beneficios de descuento")