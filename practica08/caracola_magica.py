import random

respuestas= [
    "Mi respuesta es no.",
    "Las señales apuntan a que sí.",
    "Respuesta confusa, intenta de nuevo.",
    "Sí.",
    "Puedes contar con ello.",
    "Es indudable.",
    "No se puede predecir ahora.",
    "Pregunta de nuevo más tarde.",
    "Concéntrate y pregunta de nuevo.",
    "La perspectiva es buena.",
    "Muy dudoso.",
    "Lo más probable.",
    "La perspectiva no es tan buena.",
    "Sin duda.",
    "Tal como yo lo veo, sí.",
    "Mejor no decirte ahora.",
    "No cuentes con ello.",
    "Es decididamente así.",
    "Sí, definitivamente.",
    "Mis fuentes dicen que no."
]

D="una"
while True:
    
    print("^"*50)
    print()
    opcion= str(input(f"Hola subdito, ¿quieres hacerme {D} pregunta? ")).lower()
    print()
    print("^"*50)

    if opcion == "no":
        print()
        print("-*"*25)
        print("No estas listo aun para tanta sabiduria.")
        print("-*"*25)
        print()
        break
    
    respuestas_aleatorias=random.choice(respuestas)
    D="otra"
    print("-*"*25)
    print()
    pregunta=str(input("¿Que quieres saber subdito? "))
    print()
    print("_"*50)
    print(respuestas_aleatorias)
    print("_"*50)
    print()
    print("-*"*25)

