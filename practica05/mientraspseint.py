saldodisponible= 0
inversiones= 0
monto=0
terminar= 1

print("-*SE UN INVERSIONISTA*-")
saldodisponible= int(input("Ingrese la cantidad con la que cuenta para invertir: "))

while terminar== 1:

    monto= int(input("¿Cuanto desea invertir?"))

    if saldodisponible>=monto:
        inversiones=inversiones+1
        saldodisponible=saldodisponible-monto
        print("Se realizo su ", inversiones, " inversiones con exito")
        
        if saldodisponible== "0":
            terminar=2
    else:
        print("No se pudo terminar la compra...")
        terminar=2

print ("Su saldo quedo en $",saldodisponible)
print("Con un total de ",inversiones, " inversiones")              