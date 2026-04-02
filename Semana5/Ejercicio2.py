'''Control de temperatura
Un sistema de climatización clasifica:
"Fría": menos de 10°C
"Templada": entre 10 y 25
"Calurosa": más de 25
Solicita la temperatura e indica la clasificación correspondiente.
'''
#control de temperatura
n=0
while  n==0:
    x=int(input("Ingrese la temperatura: "))
    
    if x>=25:
        print("La temperatura es Calurosa.")
    elif 9<x<25:
        print("La temperatura es Templada.")
    elif x<10:
        print("La temperatura esta Fria.")
    n = int(input("Desea ingresar otra temperatra?: Si=0/No=1: "))





