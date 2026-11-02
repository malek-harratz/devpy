L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1

elements_trouver = False
for x in L :
    if 25 <= x <= 90 :
        produit *= x
        elements_trouver = True 


        if elements_trouver:
            print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit)

        else :
            print ("Aucune valeur de la liste n'est comprise dans l'intervalle [25, 90].")


 