def calculer_investissement(montant,taux):
    return montant*taux

montant = 10000
taux = 1.02
print (f"le gain annuel est {montant}")
print (f"l'investisseur rajoute 500 € le taux passe donc à {taux + 0.02}")
taux=1.04
montant = 15000
print(f"l'année suivante l'investisseur recupèra donc {calculer_investissement(montant,taux)}")
montant = 15600
print (f"l'investisseur retire 10% de son gain, le taux descend a 1%. Ce qui le fait investir{calculer_investissement(montant*0.9,taux-1)}")
montant = 14600.6
taux = 1.03
print (f"le montant final de l'investissement etait donc {montant}, avec un taux a {taux} l'investisseur encaissera donc {calculer_investissement(montant,taux)}")



