'''Cajero automático: validación de retiro
Un cajero permite retirar solo montos mayores a 0 y múltiplos de 10.
Solicita el monto hasta que sea válido y luego muestra "Retiro exitoso".'''
#cajero
entrar =0
while entrar ==0:
    print("----------Cajero automatico----------")
    print("IMPORTANTE: el monto debe ser multiplo de 10 y mayor a 0!")
    x=int(input("Monto a retirar: "))
    if (x>0) and (x%10==0):
        print("Monto retirado: ",x,"$")
    else:
        print("El cajero solo admite montos mayores a 0 y multiplos de 10!")
    entrar= int(input("Desea realizar otra operacion?: (Si=0/No=1): "))
    



