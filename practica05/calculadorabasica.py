print()

while True:
   print ("""-*CALCULADORA BASICA*-
   1. Sumar dos numeros
   2. Restar dos numeros
   3. Multiplicar dos numeros
   4. Dividir dos numeros
   5. SALIR
   """)
   opcion= int(input("Eliga el numero de la accion deseada: "))

   if opcion== 1:
      print("Sumando...")
      num1= int(input("Ingrese el primer numero: "))
      num2= int(input("Ingrese el sgundo numero: "))
      suma=num1+num2
      print("Su total es: ",suma)
   elif opcion== 2:
      print("Restando...")
      num1= int(input("Ingrese el primer numero: "))
      num2= int(input("Ingrese el sgundo numero: "))
      resta=num1-num2
      print("Su total es: ",resta)
   elif opcion== 3:
      print("Multiplicando...")
      num1= int(input("Ingrese el primer numero: "))
      num2= int(input("Ingrese el sgundo numero: "))
      multiplicacion=num1*num2
      print("Su total es: ",multiplicacion)
   elif opcion== 4:
      print("Dividiendo...")
      num1= int(input("Ingrese el primer numero: "))
      num2= int(input("Ingrese el sgundo numero: "))
      division=num1/num2
      print("Su total es: ",division)
   elif opcion== 5:
      print("Saliendo del programa...")
      break