print()

print("-*ANALIZADOR DE TEXTOS*-")

print()

textocompleto= str(input("Ingrese el texto a analizar: "))
L1= str(input("Ingrese la primera letra a buscar: "))
L2= str(input("Ingrese la segunda letra a buscar: "))
L3= str(input("Ingrese la tercera letra a buscar: "))

print()

textocompleto=textocompleto.lower()
L1=L1.lower()
L2=L2.lower()
L3=L3.lower()

Cl1=0
Cl2=0
Cl3=0

for caracter in textocompleto:
    if caracter == L1:
        Cl1+=1
    if caracter == L2:
        Cl2+=1
    if caracter == L3:
        Cl3+=1

print("----*DATOS OBTENIDOS*----")

print()

print("la letra ",L1," aparece ",Cl1," veces en el texto.")
print()
print("la letra ",L2," aparece ",Cl2," veces en el texto.")
print()
print("la letra ",L3," aparece ",Cl3," veces en el texto.")
print()

palabrasc=0

palabras= textocompleto.split( )
for espacios in palabras:
    palabrasc=palabrasc+1

print("Hay ",palabrasc, " palabras en el texto.")

primeraL= textocompleto[0]
ultimaL= textocompleto[-1]

print()
print("Su texto inicia con la letra ",primeraL)
print()
print("Su texto termina con la letra ",ultimaL)
print()

py=0

if "python" in textocompleto:
    py='SI'
else:
    py='NO'

print("La palabra python ",py," se encuentra en el texto.")
print()

txtinverso=palabras[::-1]
print("Su texto de manera inversa es: ") 
print()
print(txtinverso)
print()

#00000280677
#Laura Fernanda Lopez Carrizosa