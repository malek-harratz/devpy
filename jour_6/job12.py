




def tri_croissant(liste):
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


print(tri_croissant([5, 2, 8, 1, 3]))