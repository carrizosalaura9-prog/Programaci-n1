import tkinter as tk
from tkinter import ttk

def saludar():
    etiqueta2.config(text="Hola, "+entrada_texto.get())


#1. Crear la ventana principal
root = tk.Tk()
root.title("Mi primer ventana (raiz)")
root.geometry("800x600") #WxH Ancho x Altura

#2. Ponemos widgets
etiqueta = ttk.Label(root,text="Nombre:",font="Helvica 20")
etiqueta.grid(row=0,column=0,padx=20,pady=20)

entrada_texto = ttk.Entry(root,font="Helvica 20")
entrada_texto.grid(row=0,column=1,padx=10,pady=20)

etiqueta2 = ttk.Label(root,font="Helvetica 30",foreground="#FFFFFF",background="#a23fed")
etiqueta2.grid(row=1,column=0,columnspan=2)

boton = ttk.Button(root,text="Esto es un boton",command=saludar,padding=20)
boton.grid(row=2,column=0,columnspan=2,padx=20,pady=20)
#boton.pack(pady=20)
#boton.place(x=200,y=100)

check = ttk.Checkbutton(
    root,
    text="Aceptas los terminos?"
)

check.grid(row=3,column=0,columnspan=2)

opcion = tk.StringVar()
opcion.set("rojo")

r1 = ttk.Radiobutton(root,text="rojo",variable=opcion,value="rojo")
r2 = ttk.Radiobutton(root,text="verde",variable=opcion,value="verde")
r3 = ttk.Radiobutton(root,text="azul",variable=opcion,value="azul")

r1.grid(row=4,column=0)
r2.grid(row=4,column=1)
r3.grid(row=4,column=2)

#3. Siempre va al final
root.mainloop() #Mantener activa la ventana y escuchando eventos
