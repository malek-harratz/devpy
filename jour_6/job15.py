def arrondir_et_trier(liste):
    
    for i in range(len_liste(liste)):
        entier = int(liste[i])
        decimal = liste[i] - entier

        if decimal >= 0.5:
            liste[i] = entier + 1
        else:
            liste[i] = entier

    
    n = 0
    for element in liste:
        n = n + 1

    for i in range(n):
        indice_min = i

        for j in range(i + 1, n):
            if liste[j] < liste[indice_min]:
                indice_min = j

        temporaire = liste[i]
        liste[i] = liste[indice_min]
        liste[indice_min] = temporaire

    return liste


def len_liste(liste):
    n = 0
    for element in liste:
        n = n + 1
    return n


nombres = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

print(arrondir_et_trier(nombres))