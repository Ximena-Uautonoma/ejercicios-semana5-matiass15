'''Registro de asistencia diaria
En una oficina se registra la asistencia hasta que el trabajador ingresa 0.
Solicita repetidamente:
1 si asistió
0 para terminar
Al final, muestra cuántos días asistió.'''
#asistencia
n=1
suma=0
x=0
while n!=0:
    print("-----------------------------------------")
    x=x+1
    print("Dia: ",x,)
    print("Indique si asistio o no asistio")
    n = int(input("(1=Asistio/0=Falto): "))
    suma=suma+n
print("Dias asistidos: ",suma)
    




