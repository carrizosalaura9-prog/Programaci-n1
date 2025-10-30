
from modelos.curso import agregar_curso

while True:

    opcion=input("""Ingrese la accion deseada:
1. Agregar curso
2. Agregar alumno
3. Dar de baja alumno
4. Mostrar
""").lower()

    cursos={}

    match opcion:
        case "1" | "agregar curso":
            while True:
                print("agregando curso")
                nombre_del_curso=input("ingrese el nombre del curso: ")
                curso_nuevo= agregar_curso()
                cursos[nombre_del_curso]= curso_nuevo
                print("Curso añadido con exito")
                print(cursos)

                print("volviendo al menu..")
                break
                
        case "2" | "agregar alumno":
            print("agregando alumno")
        case "3" | "dar de baja alumno":
            print("dando de baja alumno")
        case "4" | "mostrar":
            print("mostrando")