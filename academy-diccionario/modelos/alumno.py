def agregarAlumno():
    NombreAlumno=input("Ingrese el nombre del alumno: ")
    EdadAlumno=input ("Ingrese la edad del alumno: ")
    semestre=input("Ingrese el semestre del alumno: ")
    carrera=input("Ingrese la carrera del alumno: ")
    

    IdAlumno={
        "nombre":NombreAlumno,
        "edad":EdadAlumno,
        "semestre":semestre,
        "carrera":carrera
    }
    return IdAlumno

