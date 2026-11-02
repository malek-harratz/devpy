L = [10, 20, 30,40,50 ]
print("Deuxième valeur :", L[1])


def modifier_liste():
    L[3] = L[2] + L[4]

modifier_liste()


print("Liste modifiée :", L)

print("Dernière valeur :", L[-1])