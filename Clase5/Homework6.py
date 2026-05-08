"""
Combinacion de Ciclos
Crea un programa que imprima la tabla de multiplicar de 1 al 10 
Usa un ciclo for para los numeros del 1 al 10 y un ciclo while para calcular y mostrar los productos 
"""

numero=0
multiplicar=1
for tabla in range (1,11):
   print (" La tabla del:", tabla)
   multiplicar=1
   while multiplicar <11:
     print (tabla*multiplicar) 
     multiplicar= multiplicar + 1