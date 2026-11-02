def draw_rectangle (width,height):
    """Affiche un rectangle de width colonnes et height lignes."""
    if width < 2 or height < 2 :
        print ("le rctangle doit faire au moin 2 x 2")
        return 

    bord = "-" * width
    milieu = "|" + " " * (width - 2) + "|"

    print (bord)
    for _ in range (height - 2) :
        print (milieu)
        print (bord)

draw_rectangle (10,3)