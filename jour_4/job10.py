def verifier_pair_impair(nombre):
    if not isinstance(nombre, int) or isinstance(nombre, bool):
        print("Erreur : le nombre doit être un entier.")
    elif nombre < 0:
        print("Erreur : le nombre doit être positif.")
    elif nombre % 2 == 0:
        print(nombre, "est un nombre pair.")
    else:
        print(nombre, "est un nombre impair.")

verifier_pair_impair(7)
