def draw_triangle (height):
    for i in range (height):
        espace = ""* (height -1 - i)
        remplissage = "_" if i == height - 1 else " "
        print ( espace + "/" + remplissage * (2 * i) + "\\")


hauteur = int (input("hauteur :"))
draw_triangle (hauteur)