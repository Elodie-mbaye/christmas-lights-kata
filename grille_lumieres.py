# Taille de la grille
TAILLE = 1000

# Liste des instructions : (operation, x1, y1, x2, y2)
instructions = [
    ("on",     887,   9, 959, 629),
    ("on",     454, 398, 844, 448),
    ("off",    539, 243, 559, 965),
    ("off",    370, 819, 676, 868),
    ("off",    145,  40, 370, 997),
    ("off",    301,   3, 808, 453),
    ("on",     351, 678, 951, 908),
    ("toggle", 720, 196, 897, 994),
    ("toggle", 831, 394, 904, 860),
]

grille_on_off = []
for i in range(TAILLE):
    ligne = [0] * TAILLE
    grille_on_off.append(ligne)

for op, x1, y1, x2, y2 in instructions:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if op == "on":
                grille_on_off[x][y] = 1
            elif op == "off":
                grille_on_off[x][y] = 0
            elif op == "toggle":
                if grille_on_off[x][y] == 0:
                    grille_on_off[x][y] = 1
                else:
                    grille_on_off[x][y] = 0

compte_allumees = 0
for x in range(TAILLE):
    for y in range(TAILLE):
        compte_allumees += grille_on_off[x][y]

print("Partie 1 - Nombre de lumières allumées :", compte_allumees)


grille_lumi = []
for i in range(TAILLE):
    ligne = [0] * TAILLE
    grille_lumi.append(ligne)

for op, x1, y1, x2, y2 in instructions:
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if op == "on":
                grille_lumi[x][y] += 1
            elif op == "off":
                if grille_lumi[x][y] > 0:
                    grille_lumi[x][y] -= 1
            elif op == "toggle":
                grille_lumi[x][y] += 2

luminosite_totale = 0
for x in range(TAILLE):
    for y in range(TAILLE):
        luminosite_totale += grille_lumi[x][y]

print("Partie 2 - Luminosité totale :", luminosite_totale)
