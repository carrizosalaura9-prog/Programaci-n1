#if else elif
edad=25 #int(input("Dime tu edad:"))

if edad >= 10 and edad <18:
    print ("Eres un adolescente")
elif edad >=18:
    print("Eres un adulto")
else:
    print("Todavia eres un niño")

#match

opcion = int(input("""
1. Agregar
2. Editar
3. Eliminar
4. Leer
5. Finalizar
"""))

match opcion:
    case 1:
        print("Se ha agregado correctamente")
    case 2:
        print("Se ha modificado correctamente")
    case 3:
        print("Se ha eliminado correctamente.")
    case 4:
        print("El usuario registrado se llama Laura.")
    case 5:
        print("SE finalizara el programa.")

# barra invertida para saltar linea, barra invertida y "" para resaltar texto