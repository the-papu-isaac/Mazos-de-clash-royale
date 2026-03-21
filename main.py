
Nom_Mazos = {
    1:"Mazo Creativo",
    2:"Mazo PRO",
    3:"Mazo Rata",
    4:"Mazo UltraBait",
    5:"Mazo Bridge Spam",
    6:"Mazo 2.6 Troll",
}
print("Mazos disponibles: ", Nom_Mazos)

deck_1 = {
    1: {"Apoyo": "bruja", "Costo": 5, "Evolucion": True, "Heroe": False},
    2: {"Hechizo Grande": "bola de fuego", "Costo": 4, "Evolucion": False, "Heroe": False},
    3: {"Win condition": "ariete de batalla", "Costo": 4, "Evolucion": True, "Heroe": False}, 
    4: {"Mini-Tanque": "caballero", "Costo": 3, "Evolucion": True, "Heroe": True},
    5: {"Hechizo Pequeño": "bola de nieve", "Costo": 2, "Evolucion": True, "Heroe": False},
    6: {"Estructura": "lapida", "Costo": 3, "Evolucion": False, "Heroe": False},
    7: {"Defensa": "guardias", "Costo": 3, "Evolucion": False, "Heroe": False},
    8: {"Distracción": "duendes con lanza", "Costo": 2, "Evolucion": False, "Heroe": False},
}

deck_2 = {
    1: {"Win Condition": "rompemuros", "Costo": 2, "Evolucion": True, "Heroe": False},
    2: {"Nombre": "fantasma real", "Costo": 3, "Evolucion": True, "Heroe": False},
    3: {"Nombre": "larry", "Costo": 1, "Evolucion": True, "Heroe": False},
    4: {"Nombre": "espíritu de hielo", "Costo": 1, "Evolucion": True, "Heroe": False},
    5: {"Nombre": "barril de duendes", "Costo": 3, "Evolucion": True, "Heroe": False},
    6: {"Estructura": "torre bomber", "Costo": 4, "Evolucion": False, "Heroe": False},
    7: {"Nombre": "bola de fuego", "Costo": 4, "Evolucion": False, "Heroe": False},
    8: {"Hechizo Pequeño": "tronco", "Costo": 2, "Evolucion": False, "Heroe": False},
}

deck_3 = {
    1: {"Nombre": "Baby dragon", "Costo": 4, "Evolucion": True, "Heroe": False},
    2: {"Distracción y win condition": "Barril de esqueletos", "Costo": 3, "Evolucion": True, "Heroe": False},
    3: {"Tanque": "Rey esqueleto", "Costo": 4, "Evolucion": False, "Heroe": False},
    4: {"Win Condition": "Minero", "Costo": 3, "Evolucion": False, "Heroe": False},
    5: {"Tanque": "Mega knight", "Costo": 7, "Evolucion": True, "Heroe": False},
    6: {"Nombre": "pandilla de duendes", "Costo": 3, "Evolucion": False, "Heroe": False},
    7: {"Nombre": "Duendes con lanza", "Costo": 2, "Evolucion": False, "Heroe": False},
    8: {"Nombre": "Zap", "Costo": 2, "Evolucion": True, "Heroe": False},
}

deck_4 = {
    1: {"Nombre": "Barril de esqueletos", "Costo": 3, "Evolucion": True, "Heroe": False},
    2: {"Nombre": "Ejercito de esqueletos", "Costo": 3, "Evolucion": True, "Heroe": False},
    3: {"Tanque": "Rey esqueleto", "Costo": 4, "Evolucion": False, "Heroe": False},
    4: {"Win Condition": "Arbusto sospechoso", "Costo": 2, "Evolucion": False, "Heroe": False},
    5: {"Nombre": "Duende lanzadardos", "Costo": 3, "Evolucion": True, "Heroe": False},
    6: {"Distracción": "Duendes", "Costo": 2, "Evolucion": False, "Heroe": True},
    7: {"Nombre": "Enredadera", "Costo": 3, "Evolucion": False, "Heroe": False},
    8: {"Nombre": "Bruja madre", "Costo": 4, "Evolucion": False, "Heroe": False},
}

deck_5 = {
    1: {"Tanque": "P.E.K.K.A.", "Costo": 7, "Evolucion": True, "Heroe": False},
    2: {"Soporte": "Arquero magico", "Costo": 4, "Evolucion": False, "Heroe": True},
    3: {"Nombre": "Ariete de batalla", "Costo": 4, "Evolucion": True, "Heroe": False},
    4: {"Nombre": "Fantasma real", "Costo": 3, "Evolucion": True, "Heroe": False},
    5: {"Distracción": "Bandida", "Costo": 3, "Evolucion": False, "Heroe": False},
    6: {"Hechizo Pequeño": "Zap", "Costo": 2, "Evolucion": True, "Heroe": False},
    7: {"Hechizo Grande": "Bola de fuego", "Costo": 4, "Evolucion": False, "Heroe": False},
    8: {"Apoyo": "Mago electrico", "Costo": 4, "Evolucion": False, "Heroe": False},
}

deck_6 = {
    1: {"Nombre": "Hog rider", "Costo": 4, "Evolucion": False, "Heroe": False},
    2: {"Nombre": "Mosquetera", "Costo": 4, "Evolucion": True, "Heroe": True},
    3: {"Nombre": "Esqueletos", "Costo": 1, "Evolucion": True, "Heroe": False},
    4: {"Nombre": "Espiritu de hielo", "Costo": 1, "Evolucion": True, "Heroe": False},
    5: {"Nombre": "LOOOOOOOOOOOOOG", "Costo": 2, "Evolucion": False, "Heroe": False},
    6: {"Nombre": "Cañon", "Costo": 3, "Evolucion": True, "Heroe": False},
    7: {"Win Condition": "Sneaky Golem", "Costo": 8, "Evolucion": False, "Heroe": False},
    8: {"Hechizo Grande": "Bola de fuego", "Costo": 4, "Evolucion": False, "Heroe": False},
}

Mazos = {
    1:deck_1,
    2:deck_2,
    3:deck_3,
    4:deck_4,
    5:deck_5,
    6:deck_6,
}
m = int(input("Ingrese el Mazo a visualizar: "))

print("Estas Visualizando el " + Nom_Mazos[m])
print(Mazos[m])


m1 = int(input("Ingrese la Carta a visualizar del " + Nom_Mazos[1] + ": "))
print(Nom_Mazos[1] , deck_1[m1])

m2 = int(input("Ingrese la Carta a visualizar del " + Nom_Mazos[2]  + ": "))
print(Nom_Mazos[2], deck_2[m2])

m3 = int(input("Ingrese la Carta a visualizar del " + Nom_Mazos[3]  + ": "))
print(Nom_Mazos[3], deck_3[m3])

m4 = int(input("Ingrese la Carta a visualizar del " + Nom_Mazos[4]  + ": "))
print(Nom_Mazos[4], deck_4[m4])

m5 = int(input("Ingrese la Carta a visualizar del " + Nom_Mazos[5] + ": "))
print(Nom_Mazos[5], deck_5[m5])

m6 = int (input("Ingrese la carta a visualizar del " + Nom_Mazos[6] + ": "))
print(Nom_Mazos[6], deck_6[m6])



