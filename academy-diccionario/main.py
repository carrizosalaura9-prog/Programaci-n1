import modelos.curso
import modelos.alumno
from modelos.curso import agregarCurso
from modelos.alumno import agregarAlumno

cursos={}
alumnos={}
while True:
    print()
    print("-"*20,"ESTAS EN MENU","-"*20)
    menuopcion=input("""~ agregar
    1 -> curso
    2 -> alumno
~ modificar
    3 -> curso
    4 -> alumno
~ eliminar
    5 -> curso
    6 -> alumno
~ mostrar
    7 -> cursos
    8 -> alumnos
9 -> [SALIR]
                     
¿Que accion desea realizar?: """).lower()
    print()
    print("-"*55)

    match menuopcion:
        case "1"| "agregar curso":
            print("agregando curso")
            while True:
                NombreCurso= input("Ingrese el nombre del curso nuevo: ").lower()
                cursos[NombreCurso]=0
                cursos[NombreCurso]=agregarCurso()
                print("se ha agregado correctamente, ahora estos son los cursos disponibles: ")
                print(list(cursos.keys()))
                opcion=input("¿Desea agregar otro curso?(si/no) ")
                if opcion == "no":
                    break

        case "2"| "agregar alumno":
                print("agregando alumno")
                NombreAgAlumno=input("Ingrese el nombre del curso al que desea agregar un alumno: ").lower()
                if NombreAgAlumno in cursos:
                    print("se encontro el curso")
                    while True:
                        idAlumno=input("ingrese el ID del alumno: ")
                        cursos[NombreAgAlumno]["alumnos"][idAlumno]=agregarAlumno()
                        print("La lista de alumnos del curso: ")
                        print()
                        print(cursos[NombreAgAlumno]["alumnos"])
                        print()
                        opcion=input("¿Desea añadir otro alumno al mismo curso?: ")
                        if opcion=="no":
                            break

        case "3"| "modificar curso":
            print("modifcando curso..")
            print("Estos son los nombres de los cursos disponibles: ",list(cursos.keys()))
            nombre=input("ingrese el nombre del curso que desea modifcar: ").lower()
            if nombre in cursos:
                print("Se encontro el curso")
                nombreNuevo=str(input("Ingrese el nuevo nombre del curso: "))
                cursos[nombreNuevo]= cursos.pop(nombre)
                cursos[nombreNuevo]=agregarCurso()
                print("La lista del curso <",nombreNuevo,"> quedo asi:")
                print(cursos[nombreNuevo])
            else:
                print("No se encontro el curso.")
        
        case "4"| "modificar alumno":
            print("modificando alumno")
            nombreCMdi=input("Ingrese el nombre del curso: ").lower()
            Idmodificar=input("Ingrese el Id del alumno que desea modificar: ")
            cursos[nombreCMdi]["alumnos"][Idmodificar]=agregarAlumno()
            print("asi quedo la lista: ")
            print(cursos[nombreCMdi]["alumnos"])

        case "5"| "eliminar curso":
            print("eliminando curso")
            eliminarN=input("Ingrese el nombre del curso a eliminar: ").lower()
            cursos.pop(eliminarN)
            print("los cursos disponibles quedaron asi: ")
            print(list(cursos.keys()))

        case "6"| "eliminar alumno":
            print("eliminando alumno")
            Cursoname=input("Ingrese el nombre del curso: ").lower()
            ideliminar=input("Ingrese el ID del alumno que desea eliminar: ")
            cursos[Cursoname]["alumnos"].pop(ideliminar)
            print("quedando asi la lista:" )
            print(cursos[Cursoname]["alumnos"])

        case "7"| "mostrar cursos":
            print("mostrando cursos")
            print(list(cursos.keys()))
            while True:
                opcion=input("¿Desea conocer la lista a profundidad de un curso?(si/no) ")
                if opcion =="no":
                    break
                nombreMostrar=input("Ingrese el nombre del curso: ").lower()
                print(cursos[nombreMostrar])

        case "8"| "mostrar alumnos":
            print("mostrando alumnos")
            cursoNombre=input("Ingrese el nombre del curso: ").lower()
            print("La lista de alumnos quedo asi: ")
            print(cursos[cursoNombre]["alumnos"])

        case "9"| "salir":
            print("saliendo del programa...")
            break