def cifrar_mensaje(mensaje, clave):
    resultado = ""
    for letra in mensaje:
        if letra.isalpha():
            if letra.isupper():
                base = ord('A')
            else:
                base = ord('a')
            nuevaletra = chr((ord(letra) - base + clave) % 26 + base)
            resultado = resultado + nuevaletra

        elif letra.isdigit():
            resultado = resultado + letra

        elif letra == " ":
            resultado = resultado + "_"

        else:
            if clave % 2 == 0:
                resultado = resultado + "@"
            else:
                resultado = resultado + "!"
    return resultado


def iniciar():
    while True:
        print("()"*25)
        print("----*CIFRADOR DE MENSAJES*----")
        print()
        print("""1. Cifrartexto.
2. Descifrartexto.
3. Salir.""")
        print()
        opcion = input("Seleccione la accion deseada: ")
        print()
        print("()"*25)
        print()

        match opcion:
            case "1" | "cifrar"|"cifrartexto":
                print()
                print("()"*25)
                mensaje = input("Escriba el mensaje: ")
                print()
                clave = int(input("Escribe la clave: "))
                print()
                resultado = cifrar_mensaje(mensaje, clave)
                print("Su texto cifrado es: ", resultado)
                print()
                print("()"*25)
                print()
        
            case "2":
                print()
                print("()"*25)
                mensaje = input("Escribe el mensaje cifrado: ")
                print()
                clave = int(input("Escribe la clave usada: "))
                print()
                resultado = cifrar_mensaje(mensaje, -clave)
                print("Su mensaje descifrado es:", resultado)
                print("()"*25)
                print()

            case "3":
                print()
                print("Saliendo... ")
                print()
                print("()"*25)
                break

iniciar()
