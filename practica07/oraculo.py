
def iniciar():
    while True:
        print("_"*50)
        opcion= input("¿Deseas conocer tu destino? (si/no): ").lower()
        print()
        if opcion == "no":
            print("Esto esta siendo demasiado para ti, lo entiendo, vuelve pronto!.")
            break

        nombre= input("Te estaba esperando, recuerdame tu nombre. ")
        print()
        anio= int(input(f"En que año naciste {nombre} ? "))
        print()
        numero_de_la_suerte= int(input(f"Ahora {nombre}, dime un numero del 1 al 4. "))
        print()
        elemento= calcular_elemento(anio)
        print("<>"*25)
        prediccion= generar_prediccion(nombre,elemento,numero_de_la_suerte)
        print("<>"*25)



def calcular_elemento (anio):
    elemento=(anio%10)
    match elemento:
        case 0 | 1: return "metal"
        case 2 | 3: return "agua"
        case 4 | 5: return "madera"
        case 6 | 7: return "fuego"
        case 8 | 9: return "tierra"

def generar_prediccion (nombre,elemento,numero_de_la_suerte):
    match numero_de_la_suerte:
        case 1:
            print(f"Hola {nombre}, haz sido una persona bendecida al tener el elemento de {elemento}, es buen momento para aprovecharlo y comprar un boleto de loteria.")
        case 2:
            print(f"Un gusto verte {nombre}, eres una persona dificl de tratar, ya que al ser del elemento de {elemento}, eres un poco salado, hazte una limpia.")
        case 3:
            print(f"Te saludo a ti {nombre}, eres un elemento de {elemento}, y al serlo, te hace ser alguien distraido, checa mas tus pies y puede que el destino te premie.")
        case 4:
            print(f"Te estaba esperando {nombre}, eres abundancia y tu elemento de {elemento}, no puede ser un complemento mejor, ese proyecto que tienes en mente es para ti, no dudes de ti y el destino te premiara.")
        case _:
            print(f"Eres una persona retadora {nombre}, me gusta, claramente eres un elemento de {elemento}, no hay mas que decir para darse cuenta de ello, recuerda que de vez en cuando esta bien no seguir reglas, pero no TODO el tiempo.")

iniciar()