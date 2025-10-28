info_tienda=("La diversion si tiene precio",2025)

print(info_tienda)
print()

inventario={
    "GTA":{"precio":500,"stock":10},
    "pacman":{"precio":50,"stock":20},
    "MarioBros":{"precio":10,"stock":5}
}

print("este es el inventario")
print()
print(inventario)
print("Precio del segundo juego PACMAN")
print()
print(inventario["pacman"]["precio"])
print("Ahora vendi una copia de GTA, quedando asi: ")
print()
inventario["GTA"]["stock"]=9
print(inventario)
