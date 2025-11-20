import tkinter as tk
#Crecion de la ventana principal
root = tk.Tk()
root.title("CALCULADORA")
root.geometry("300x425")

#Agregar widgets
botones_texto = (
    "C","/","*","-",
    "7","8","9","+",
    "4","5","6","",
    "1","2","3","=",
    "0","",".",""
    )

#width caracteres, fill se llena (both), justify se justifica el txt
historico = tk.Label(root,bg="#a40cc6",font="Roboto 14",width=15,bd=0)
historico.pack(pady=5,padx=10,fill="x")

resultado = tk.Entry(root,bg="#d196eb",bd=1,font="Roboto 24",width=15,justify="right")
resultado.pack(padx=10,fill="x")

contenedor_botones = tk.Frame(root,bg="#a40cc6")
contenedor_botones.pack(pady=5,padx=10,fill="both")

acumulador=0
for row in range(5):#0
    for column in range(4):#0
        boton = tk.Button(contenedor_botones,text=botones_texto[acumulador],bg="#d196eb",
            fg="#000000",font="Roboto 20",width=3,height=1)
        if botones_texto[row+column] !=" ":
           

            if botones_texto[acumulador] =="+":
                boton.config(height=3)
                boton.grid(row=row,column=column,padx=1,pady=5,rowspan=2)

            if botones_texto[acumulador] =="=":
                boton.config(height=3)
                boton.grid(row=row,column=column,padx=1,pady=5,rowspan=2)

            if botones_texto[acumulador] =="0":
                boton.config(width=8)
                boton.grid(row=row,column=column,padx=1,pady=5,columnspan=2)

            elif botones_texto[acumulador] =="":
                hola=0

            else:
                boton.grid(row=row,column=column,padx=5,pady=5)

            

        acumulador+=1

root.mainloop()