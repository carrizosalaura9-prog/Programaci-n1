
def agregarCurso():
    
    NombreInstructor=input("Ingrese el nombre del instructor: ")
    TituloInstructor=input("Ingrese el titulo del instructor: ")
    EdadInstructor=input ("Ingrese la edad del instructor: ")
    NumeroAula=input("Ingrese el aula en la que se llevara a cabo: ")
    
    cursos= {
        "instructor":{
            "nombre": NombreInstructor,
            "titulo": TituloInstructor,
            "edad": EdadInstructor
        },
        "aula": NumeroAula,
        "alumnos": {}
        }
    return cursos

