from main import nombre_del_curso
from main import cursos


def agregar_curso():
    instructor={}
    
    nombre_instructor=input("ingrese el nombre del instructor: ")
    titulo_instructor=input("ingrese el titulon del instructor: ")
    edad_instructor=input("ingrese la edad del instructor: ")
    aula=input("ingrese el aula en la que se llevara a cabo el curso: ")



    instructor = {
        "nombre": nombre_instructor,
        "titulo": titulo_instructor,
        "edad": edad_instructor,
    }

    curso = {
        "instructor": instructor,
        "aula": aula,
        "alumnos": {}
    }


    cursos[nombre_del_curso] = curso

    return curso





    