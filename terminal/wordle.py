import random
palabras = ("abeto","actor","aguas","agudo","alado",
            "albas","altar","anton","actor","azul")


while True:
    palabra = palabras[random.randint(0,len(palabras)-1)]
    wordle=list(palabra)
    print("""\033[1;35m
========================[WORDLE]=========================
Bienvenido, ya haz elegido la palabra, tienes 5 intentos.
=========================================================
\033[0;37m""")
    
    for i in range(5):
        intento=input("Ingrese una palabra de 5 letras sin acentos.").lower()[:5]
        indice=0
        resultado=""
        correctas=0
        for letra in intento:
            if letra == wordle[indice]:
                correctas+=1
                resultado+="\033[1;32m"+letra+"\033[0;37m"
            elif letra in wordle:
                resultado+="\033[1;33m"+letra+"\033[0;37m"
            else:
                resultado+="\033[1;31m"+letra+"\033[0;37m"
            indice+=1
        print(resultado)

        if correctas == 5:
            break

    if correctas == 5:
        print(f"Felicidades la palabra era \033[1;32m{palabra}\033[0;37m has acertado.")
    else:
        print(f"Lo siento no haz adivinado la palabra \033[1;31m{palabra}\033[0;37m ")

    opcion = input("¿Desea jugar otra ronda?(si/no) ").lower()

    if opcion == "no":
        break

