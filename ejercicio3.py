"""
Biblioteca
La biblioteca permite retirar libros solo si el usuario no tiene devoluciones pendientes. 
Consigna: Pedir el estado del usuario (pendiente o no) y mostrar si puede retirar libros.
"""

print ("---BIENVENIDOS A LA BIBLIOTECA---")

#usamos .lower() : transforma todo en minuscula

estado= input ("En que estado se encuentra, ¿Pendiente o Activo?").lower()

if estado == "pendiente":
    print ("No puede retirar, porque tiene devoluciones pendientes")

elif estado == "activo":
    print ("Si puede retirar libros")

else:
    print ("A ingresado un valor incorrecto. Solo puede escribir Pendiente o Activo")

