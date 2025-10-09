print()

print("-*ASISTENTE DE DESICIONES DEL DIA*-")

print()

dia= input("¿Que dia de la semana es? ")

print()

match dia:
    case "lunes":
        Semana= "Entre"
    case "martes":
        Semana= "Entre"
    case "miercoles":
        Semana= "Entre"
    case "jueves":
        Semana= "Entre"
    case "viernes":
        Semana= "Entre"
    case "sabado":
        Semana= "Fin" 
    case "domingo":
        Semana= "Fin" 

clima= input("¿Como esta el clima? ")

print()

match clima:
    case "soleado":
        if Semana== "Fin":
           print("Es un dia perfecto para ir a la playa.")
        else:
           print("Puedes trabajar y tomar el sol en tu hora de descanso.")
    case "frio":
        if Semana== "Fin":
            print("Toma tu cobija y un cafe caliente, es un dia excelente para no salir y quedarse viendo una peli.")
        else:
            print("Abrigate bien antes de salir al trabajo.")
    case "lluvioso":
        if Semana== "Fin":
            print("Hablale a una amistad y salgan a jugar bajo la lluvia.")
        else:
            print("Si no quieres llegar empapado al trabajo lleva tu paraguas.")