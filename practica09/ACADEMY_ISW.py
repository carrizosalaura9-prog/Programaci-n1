Lista_de_cursos=[]
Lista_de_alumnos=[]

def menu(Lista_de_cursos,Lista_de_alumnos):
    print()
    print("^^^^^^ACADEMY ISW^^^^^^")
    print()
    while True:
        menu_opciones=str(input("""____INGRESE LA ACCION DESEADA____
1. Agregar
2. Eliminar
3. Modificar
4. Mostrar
5. Salir
"""))
    
        match menu_opciones:
            case "1":
                menu_opciones=str(input("""____INGRESE LA ACCION DESEADA (AGREGAR)____
1. Cursos
2. Alumnos
"""))
                if menu_opciones=="1":
                    agregar_cursos(Lista_de_cursos,Lista_de_alumnos)

                if menu_opciones=="2":
                    agregar_alumnos(Lista_de_cursos,Lista_de_alumnos)

                else:
                    print("Esa opcion no esta disponible...")

            case "2":
                menu_opciones=str(input("""____INGRESE LA ACCION DESEADA (ELIMINANDO)____
1. Cursos
2. Alumnos
"""))
                if menu_opciones=="1":
                    eliminar_curso(Lista_de_cursos,Lista_de_alumnos)

                if menu_opciones=="2":
                    eliminar_alumno(Lista_de_cursos,Lista_de_alumnos)

                else:
                    print("Esa opcion no esta disponible...")

            case "3":
                menu_opciones=str(input("""____INGRESE LA ACCION DESEADA (MODIFICANDO)____
1. Cursos
2. Alumnos
3. Instructor
4. Aula
"""))
                if menu_opciones=="1":
                    modificar_curso(Lista_de_cursos,Lista_de_alumnos)

                if menu_opciones=="2":
                    modificar_alumno(Lista_de_cursos,Lista_de_alumnos)

                if menu_opciones=="3":
                    modificar_instructor(Lista_de_cursos,Lista_de_alumnos)
                if menu_opciones=="4":
                    modificar_aula(Lista_de_cursos,Lista_de_alumnos)
                else:
                    print("Esa opcion no esta disponible...")  

            case "4":
                menu_opciones=str(input("""____INGRESE LA ACCION DESEADA (MOSTRANDO)____
1. Cursos
2. Alumnos
"""))
                if menu_opciones=="1":
                    mostrar_cursos(Lista_de_cursos,Lista_de_alumnos)

                if menu_opciones=="2":
                    mostrar_alumnos(Lista_de_cursos,Lista_de_alumnos)
            case "5":
                print()
                print("^^^^^^SALIENDO DEL PROGRAMA^^^^^^")
                print()
    
                break

def agregar_cursos(Lista_de_cursos,Lista_de_alumnos):
    print("^"*20,"-GENERANDO CURSO-","^"*20)
    while True:
        print()
        nombre_del_curso=input("Ingrese el nombre del curso: ")
        print()
        instructor=input("¿Cual es el nombre del instructor? ")
        print()
        aula=input("Ingrese el aula en la cual se llevara a cabo el curso: ")
    
        while True:
            print()
            alumnos=input("Ingrese el nombre del alumno: ")
            Lista_de_alumnos.append(alumnos)
            print()
            opcion_seguir_agregando_alumnos_=input("¿Desea seguir agregando alumnos?(si/no) ")

            if opcion_seguir_agregando_alumnos_=="no":
                Lista_de_cursos.append(nombre_del_curso)
                Lista_de_cursos.append(instructor)
                Lista_de_cursos.append(aula)
                Lista_de_cursos.append(Lista_de_alumnos)
                print()
                print("Se genero el curso exitosamente, quedando de esta manera:" ,Lista_de_cursos)
                print()
                Lista_de_alumnos=[]
                break

        opcion_agregar_otro_curso=input("¿Desea añadir otro curso?(si/no) ")

        if opcion_agregar_otro_curso=="no" or opcion_agregar_otro_curso== "n":
            print("^"*20,"-SALIENDO AGREGAR CURSOS-","^"*20)
            #menu(Lista_de_cursos,Lista_de_alumnos)
            break
            

def agregar_alumnos(Lista_de_cursos,Lista_de_alumnos):
    cursos_existentes=Lista_de_cursos
    alumnos_existentes=Lista_de_alumnos

    print()
    print("^"*20,"-AGREGANDO ALUMNOS-","^"*20)
    print()

    while True:


        curso_a_aniadir_alumno=input("Ingrese el nombre del curso al que desea añadir un alumno: ")

        if curso_a_aniadir_alumno in cursos_existentes:
            print()
            print("Se encontro exitosamente el curso.")
        else:
            print("El curso no se encontro...")

        while True:
            print()
            nombre_alumno_aniadir_=input("Ingrese el nombre del alumno a añadir: ")
            print()
            ubicacion_del_curso=cursos_existentes.index(curso_a_aniadir_alumno)
            ubicacion_de_lista_de_alumnos=ubicacion_del_curso+3
            Lista_de_cursos[ubicacion_de_lista_de_alumnos].append(nombre_alumno_aniadir_)
            opcion_seguir_agregando=input("¿Desea agregar otro alumno en el mismo curso?(si/no) ")

            if opcion_seguir_agregando == "no" or opcion_seguir_agregando == "n":
                print(Lista_de_cursos)
                break
        
        print()
        aniadir_en_otro_curso=input("¿Desea añadir un alumno en otro curso?(si/no) ")

        if aniadir_en_otro_curso == "no" or aniadir_en_otro_curso == "n":
            print("^"*20,"-SALIENDO DE AGREGAR ALUMNOS-","^"*20)
            menu(Lista_de_cursos,Lista_de_alumnos)

            break
        
def eliminar_curso(Lista_de_cursos,Lista_de_alumnos):
    print()
    print("^"*20,"-ELIMINANDO CURSO-","^"*20)
    
    while True:
        ubicacion_del_curso_a_eliminar=0
        nombre_curso_a_eliminar=input("ingrese el nombre del curso que desea eliminar: ")
        ubicacion_del_curso_a_eliminar=Lista_de_cursos.index(nombre_curso_a_eliminar)
        Lista_de_cursos.pop(ubicacion_del_curso_a_eliminar)
        print("se elimino correctamnete el curso quedando de esta forma:")
        Lista_de_cursos.pop(ubicacion_del_curso_a_eliminar)
        Lista_de_cursos.pop(ubicacion_del_curso_a_eliminar)
        Lista_de_cursos.pop(ubicacion_del_curso_a_eliminar)
        print(Lista_de_cursos)
        opcion_seguir_eliminando=input("¿Desea eliminiar otro curso?(si/no) ")
        if opcion_seguir_eliminando=="no":
            print()
            print("^"*20,"-SALIENDO DE ELIMINAR CURSO-","^"*20)
            menu(Lista_de_cursos,Lista_de_alumnos)

            break

def eliminar_alumno(Lista_de_cursos,Lista_de_alumnos):
    print()
    print("^"*20,"-ELIMINANDO ALUMNO-","^"*20)

    nombre_curso=input("Ingrese el nombre del curso en el que desea eliminar a un alumno: ")
    
    while True:
        ubi_curso=0
        nombre_alumno_a_eliminar=input("¿Cual es el nombre del alumno que desea eliminar? ")
        ubi_curso=Lista_de_cursos.index(nombre_curso)
        ubi_curso=ubi_curso+3
        print(ubi_curso)
        Lista_de_cursos[ubi_curso].remove(nombre_alumno_a_eliminar)
        print("quedando asi: ")
        print(Lista_de_cursos)
        opcion_seguir_eliminando=input("¿Desea eliminiar otro alumno?(si/no) ")
        if opcion_seguir_eliminando=="no":
            print()
            print("^"*20,"-SALIENDO DE ELIMINAR ALUMNO-","^"*20)
            menu(Lista_de_cursos,Lista_de_alumnos)

            break

def modificar_curso(Lista_de_cursos,Lista_de_alumnos):
    print("^"*20,"-MODIFICANDO CURSO-","^"*20)

    while True:
        ubi=0
        curso_a_modificar=input("¿Cual es el nombre del curso en el que desea modificar? ")
        ubi=Lista_de_cursos.index(curso_a_modificar)
        nuevo=input("Ingrese el nuevo nombre del curso: ")
        Lista_de_cursos[ubi]=nuevo

        opcion=input("¿Desea modificar otro curso?(si/no) ")

        if opcion=="no":
            print("^"*20,"-SALIENDO MODIFICAR CURSO-","^"*20)

            menu(Lista_de_cursos,Lista_de_alumnos)

            break

def modificar_instructor(Lista_de_cursos,Lista_de_alumnos):
    print("^"*20,"-MODIFICANDO INSTRUCTOR-","^"*20)

    while True:
        ubi=0
        curso_a_modificar=input("¿Cual es el nombre del curso en el que desea modificar? ")
        ubi=Lista_de_cursos.index(curso_a_modificar)
        ubi=+1
        nuevo=input("Ingrese el nuevo nombre del instructor: ")
        Lista_de_cursos[ubi]=nuevo

        opcion=input("¿Desea modificar en otro curso?(si/no) ")

        if opcion=="no":
            print("^"*20,"-SALIENDO MODIFICANDO INSTRUCTOR-","^"*20)

            menu(Lista_de_cursos,Lista_de_alumnos)

            break

def modificar_aula(Lista_de_cursos,Lista_de_alumnos):
    print("^"*20,"-MODIFICANDO AULA-","^"*20)

    while True:
        ubi=0
        curso_a_modificar=input("¿Cual es el nombre del curso en el que desea modificar? ")
        ubi=Lista_de_cursos.index(curso_a_modificar)
        ubi=+2
        nuevo=input("Ingrese el nuevo nombre del aula: ")
        Lista_de_cursos[ubi]=nuevo

        opcion=input("¿Desea modificar en otro curso?(si/no) ")

        if opcion=="no":
            print("^"*20,"-SALIENDO MODIFICANDO AULA-","^"*20)

            menu(Lista_de_cursos,Lista_de_alumnos)

            break

def modificar_alumno(Lista_de_cursos,Lista_de_alumnos):
    print("^"*20,"-MODIFICANDO ALUMNO-","^"*20)

    while True:
        ubi=0
        curso_a_modificar=input("¿Cual es el nombre del curso en el que desea realizar cambios? ")
        ubi=Lista_de_cursos.index(curso_a_modificar)
        ubi=+3
        viejo=input("Ingrese el nombre que desea modificar: ")
        ubi_nombre=Lista_de_cursos.index(viejo)
        nuevo=input("Ingrese el nuevo nombre : ")
        Lista_de_cursos[ubi][ubi_nombre]=nuevo

        opcion=input("¿Desea modificar otro curso?(si/no) ")

        if opcion=="no":
            print("^"*20,"-SALIENDO MODIFICANDO ALUMNO-","^"*20)

            menu(Lista_de_cursos,Lista_de_alumnos)

            break

def mostrar_cursos(Lista_de_cursos,Lista_de_alumnos):
    print()
    print("^"*20,"-MOSTRANDO CURSOS-","^"*20)

    print("LA LISTA DE INFORMACION DE LOS CURSOS ES:")
    lista=len(Lista_de_cursos)
    print("Hay ",lista/4," cursos disponibles")
    for i in range(0, len(Lista_de_cursos), 4):
        print(Lista_de_cursos[i:i+4])
    print("^"*20,"-SALIENDO DE MOSTRANDO CURSOS-","^"*20)
    menu(Lista_de_cursos,Lista_de_alumnos)

def mostrar_alumnos(Lista_de_cursos,Lista_de_alumnos):
        print()
        ubi_1=0
        ubi_2=0
        print("^"*20,"-MOSTRANDO ALUMNOS-","^"*20)
        print()
        curso_n=input("Ingrese el nombre del curso: ")
        print()
        ubi_1=Lista_de_cursos.index(curso_n)
        ubi_2=ubi_1+3
        mostar= Lista_de_cursos[ubi_2]
        print(mostar)
        print("^"*20,"-SALIENDO DE MOSTRANDO ALUMNOS-","^"*20)
        menu(Lista_de_cursos,Lista_de_alumnos)


menu(Lista_de_cursos,Lista_de_alumnos)


