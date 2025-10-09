print("""-*INSTITUTO TECNOLOGICO DE SONORA*-
Programacion 1 c/Lab
Examen unidad 1
 """)
calificacion=0

print()

nombre= input("Nombre completo:")
id= input("Ingrese su ID:")

print()

pregunta1= int(input("""1- ¿Cual de los siguientes componentes NO es parte fundamental de la arquitectura Von?
1. Tarjeta grafica 
2. Memoria principal
3. Sistema de entrada/salida
4. CPU
"""))

print()

match pregunta1:
    case 1:
        print("Respuesta correcta")
        calificacion= calificacion +10
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4:
        print("Respuesta incorrecta")  

print()

pregunta2= int(input("""2- El lenguaje maquina esta compuesto por:
1. Simbolos logicos y matematicos 
2. Pseudocodigo
3. Instrucciones en ingles abreviado
4. Codigo binario
"""))

print()

match pregunta2:
    case 1:
        print("Respuesta incorrecta")
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4: 
        print("Respuesta correcta")
        calificacion= calificacion +10

print()

pregunta3= int(input("""3- Un lenguaje de alto nivel se caracteriza por:
1. Ser el mas rapido en tiempo de ejecucion
2. Tener un control directo y preciso sobre el hardware
3. Ser independiente de la arquitectura de la computadora
4. Ser muy dificl de aprender y leer
"""))

print()

match pregunta3:
    case 1:
        print("Respuesta incorrecta")
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta correcta")
        calificacion= calificacion +10
    case 4:
        print("Respuesta incorrecta")

print()

pregunta4= int(input("""4- ¿Que es un algoritmo?
1. Una secuencia de pasos finitos y bien definidos para resolver un problema 
2. Un lenguaje de programacion especifico
3. El codigo fuente de un programa de computadora
4. Un conjunto de instrucciones escritas en codigo binario
"""))

print ()

match pregunta4:
    case 1:
        print("Respuesta correcta")
        calificacion= calificacion +10
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4:
        print("Respuesta incorrecta")  

print()

pregunta5= int(input("""5- En pseudocodigo, ¿Que estructura de control se utiliza para ejecutar un bloque de codigo solo si se cumple una condicion especifica?
1. Repetitiva 'mientras'
2. Repetitiva 'para'
3. Secuencial
4. Condicional o de seleccion
"""))

print()

match pregunta5:
    case 1:
        print("Respuesta incorrecta")
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4: 
        print("Respuesta correcta")
        calificacion= calificacion +10

print ()

pregunta6= int(input("""6- El proposito principal del pseudocodigo es:
1. Traducir automaticamente codigo de alto nivel a lenguaje maquina  
2. Planificar y describir la logica de un algoritmo de forma legible para los humanos 
3. Ejecutar programas de forma mas eficiente que un lenguaje compilado
4. Proporcionar un conttrol directo sobre los registros del procesador
"""))

print()

match pregunta6:
    case 1:
        print("Respuesta incorrecta")
    case 2:
       print("Respuesta correcta")
       calificacion= calificacion +10 
    case 3:
        print("Respuesta incorrecta")
    case 4:
        print("Respuesta incorrecta")

print ()

pregunta7= int(input("""7- Un programa de computadora es esencialmente:
1. Una coleccion de algoritmos
2. El sistema operativo de una computadora
3. Un dispositivo de hardware
4. Una secuencia de instrucciones que la computadora ejecuta
"""))

print ()

match pregunta7:
    case 1:
        print("Respuesta incorrecta")
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4: 
        print("Respuesta correcta")
        calificacion= calificacion +10

print ()

pregunta8= int(input("""8- ¿Cual es la principal diferencia entre un bluce MIENTRAS while y un bucle REPETIR do'while?
1. No hay ninguna diferencia, son intercambiables
2. El bucle REPETIR solo suma numeros, mientrs que el MIENTRAS puede usar cualquier condicion
3. El bucle MIENTRAS es mas rapido que el REPETIR
4. El bucle MIENTRAS puede no ejecutarse, mientras que el REPETIR se ejecuta al menos una vez
"""))

print()

match pregunta8:
    case 1:
        print("Respuesta incorrecta")
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4: 
        print("Respuesta correcta")
        calificacion= calificacion +10

print()

pregunta9= int(input("""9- El lenguaje ensamblador es considerado un lenguaje de nivel...
1. Medio
2. Alto
3. Bajo
4. Muy alto
"""))

print()

match pregunta9:
    case 1:
        print("Respuesta incorrecta")
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta correcta")
        calificacion= calificacion +10
    case 4:
        print("Respuesta incorrecta")

print()

pregunta10= int(input("""10- ¿Que estructura de control es mas adecuada para iterar sobre una secuencia de elementos un numero de veces conocido de antemano?1. Bucle PARA
2. Sentencia condicional SI
3. Bucle REPETIR
4. Bucle MIENTRAS                  
"""))

print()

match pregunta10:
    case 1:
        print("Respuesta correcta")
        calificacion= calificacion +10
    case 2:
        print("Respuesta incorrecta")
    case 3:
        print("Respuesta incorrecta")
    case 4:
        print("Respuesta incorrecta")  

print()

print("Su calificacion final es: ",calificacion)
