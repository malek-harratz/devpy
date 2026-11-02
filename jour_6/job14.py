def my_long_word(n, phrase):
    resultat = ""
    mot = ""
    longueur = 0

    for caractere in phrase + " ":
        if caractere != " " and caractere != ",":
            mot = mot + caractere
            longueur = longueur + 1
        else:
            if longueur > n:
                if resultat != "":
                    resultat = resultat + " "
                resultat = resultat + mot

            mot = ""
            longueur = 0

    return resultat


phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

print(my_long_word(3, phrase))