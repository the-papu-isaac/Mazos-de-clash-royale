
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
    3: {"Win Condition": "ariete de batalla", "Costo": 4, "Evolucion": True, "Heroe": False}, 
    4: {"Mini-Tanque": "caballero", "Costo": 3, "Evolucion": True, "Heroe": True},
    5: {"Hechizo Pequeño": "bola de nieve", "Costo": 2, "Evolucion": True, "Heroe": False},
    6: {"Estructura": "lapida", "Costo": 3, "Evolucion": False, "Heroe": False},
    7: {"Defensa": "guardias", "Costo": 3, "Evolucion": False, "Heroe": False},
    8: {"Distracción": "duendes con lanza", "Costo": 2, "Evolucion": False, "Heroe": False},
}

deck_2 = {
    1: {"Win Condition": "rompemuros", "Costo": 2, "Evolucion": True, "Heroe": False},
    2: {"Mini-Tanque": "fantasma real", "Costo": 3, "Evolucion": True, "Heroe": False},
    3: {"Distracción y Ciclado": "larry", "Costo": 1, "Evolucion": True, "Heroe": False},
    4: {"Distracción y Ciclado": "espíritu de hielo", "Costo": 1, "Evolucion": True, "Heroe": False},
    5: {"Win Condition": "barril de duendes", "Costo": 3, "Evolucion": True, "Heroe": False},
    6: {"Estructura": "torre bomber", "Costo": 4, "Evolucion": False, "Heroe": False},
    7: {"Hechizo Grande": "bola de fuego", "Costo": 4, "Evolucion": False, "Heroe": False},
    8: {"Hechizo Pequeño": "tronco", "Costo": 2, "Evolucion": False, "Heroe": False},
}

deck_3 = {
    1: {"Apoyo": "Baby dragon", "Costo": 4, "Evolucion": True, "Heroe": False},
    2: {"Distracción y Win Condition": "Barril de esqueletos", "Costo": 3, "Evolucion": True, "Heroe": False},
    3: {"Tanque": "Rey esqueleto", "Costo": 4, "Evolucion": False, "Heroe": False},
    4: {"Win Condition": "Minero", "Costo": 3, "Evolucion": False, "Heroe": False},
    5: {"Tanque": "Mega knight", "Costo": 7, "Evolucion": True, "Heroe": False},
    6: {"Distracción": "pandilla de duendes", "Costo": 3, "Evolucion": False, "Heroe": False},
    7: {"Ciclado": "Duendes con lanza", "Costo": 2, "Evolucion": False, "Heroe": False},
    8: {"Hechizo Pequeño": "Zap", "Costo": 2, "Evolucion": True, "Heroe": False},
}

deck_4 = {
    1: {"Win Condition y Distracción": "Barril de esqueletos", "Costo": 3, "Evolucion": True, "Heroe": False},
    2: {"Defensa": "Ejercito de esqueletos", "Costo": 3, "Evolucion": True, "Heroe": False},
    3: {"Tanque": "Rey esqueleto", "Costo": 4, "Evolucion": False, "Heroe": False},
    4: {"Win Condition": "Arbusto sospechoso", "Costo": 2, "Evolucion": False, "Heroe": False},
    5: {"Soporte": "Duende lanzadardos", "Costo": 3, "Evolucion": True, "Heroe": False},
    6: {"Distracción": "Duendes", "Costo": 2, "Evolucion": False, "Heroe": True},
    7: {"Hechizo Pequeño": "Enredadera", "Costo": 3, "Evolucion": False, "Heroe": False},
    8: {"Apoyo y Defensa": "Bruja Madre", "Costo": 4, "Evolucion": False, "Heroe": False},
}

deck_5 = {
    1: {"Tanque": "P.E.K.K.A.", "Costo": 7, "Evolucion": True, "Heroe": False},
    2: {"Soporte": "Arquero magico", "Costo": 4, "Evolucion": False, "Heroe": True},
    3: {"Win Condition y Distracción": "Ariete de batalla", "Costo": 4, "Evolucion": True, "Heroe": False},
    4: {"Mini-Tanque": "Fantasma real", "Costo": 3, "Evolucion": True, "Heroe": False},
    5: {"Distracción": "Bandida", "Costo": 3, "Evolucion": False, "Heroe": False},
    6: {"Hechizo Pequeño": "Zap", "Costo": 2, "Evolucion": True, "Heroe": False},
    7: {"Hechizo Grande": "Bola de fuego", "Costo": 4, "Evolucion": False, "Heroe": False},
    8: {"Apoyo": "Mago electrico", "Costo": 4, "Evolucion": False, "Heroe": False},
}

deck_6 = {
    1: {"Win Condition": "Hog rider", "Costo": 4, "Evolucion": False, "Heroe": False},
    2: {"Soporte": "Mosquetera", "Costo": 4, "Evolucion": True, "Heroe": True},
    3: {"Distracción y Ciclado": "Esqueletos", "Costo": 1, "Evolucion": True, "Heroe": False},
    4: {"Distracción y Ciclado": "Espiritu de hielo", "Costo": 1, "Evolucion": True, "Heroe": False},
    5: {"Hechizo Pequeño": "LOOOOOOOOOOOOOG", "Costo": 2, "Evolucion": False, "Heroe": False},
    6: {"Estrucutura": "Cañon", "Costo": 3, "Evolucion": True, "Heroe": False},
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

if m <= 6:
    print()
    print(Nom_Mazos[m])
    print()
    print(Mazos[m])
    print()
    c = int(input("Ingrese la Carta a visualizar del " + Nom_Mazos[m] + ": "))
    if c <= 8:
        if m == 1:
                print(deck_1[c])
        elif m == 2:
                print(deck_2[c])
        elif m == 3: 
                print(deck_3[c])
        elif m == 4: 
                print(deck_4[c])
        elif m == 5: 
                print(deck_5[c])
        elif m == 6: 
                print(deck_6[c])    
    else:
      print("Seleccionastes una carta NO DISPONIBLE del " + Nom_Mazos[m])     
else:
    print("Seleccionaste un Mazo NO DISPONIBLE")


