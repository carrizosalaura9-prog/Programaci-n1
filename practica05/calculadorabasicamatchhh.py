print()

while True:
   print ("""-*CALCULADORA BASICA*-
   1. Sumar dos numeros
   2. Restar dos numeros
   3. Multiplicar dos numeros
   4. Dividir dos numeros
   5. SALIR
   """)

   print()

   Opcion= input("Eliga el numero de la accion deseada: ")

   match Opcion:
      case 1:
         print("Sumando...")
         num1= int(input("Ingrese el primer numero: "))
         num2= int(input("Ingrese el sgundo numero: "))
         suma=num1+num2
         print("Su total es: ",suma)
      case 2:
         print("Restando...")
         num1= int(input("Ingrese el primer numero: "))
         num2= int(input("Ingrese el sgundo numero: "))
         resta=num1-num2
         print("Su total es: ",resta)
      case 3:
         print("Multiplicando...")
         num1= int(input("Ingrese el primer numero: "))
         num2= int(input("Ingrese el sgundo numero: "))
         multiplicacion=num1*num2
         print("Su total es: ",multiplicacion)
      case 4:
         print("Dividiendo...")
         num1= int(input("Ingrese el primer numero: "))
         num2= int(input("Ingrese el sgundo numero: "))
         division=num1/num2
         print("Su total es: ",division)
      
   if Opcion== "5":
      print ("Saliendo del programa...")
      break