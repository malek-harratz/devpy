n = int (input("note 1:"))
note = int (input ("note 2 :"))
no = int(input("note 3 :"))

def moyenne (no,note,n):
    moyenne_etudiant = n+note+n
    print (moyenne_etudiant/3)
    if moyenne_etudiant >= 15 and moyenne_etudiant <= 20:
        print("Très bon élève")
    elif moyenne_etudiant >= 11 and moyenne_etudiant < 15:
        print("Bon élève")
    elif moyenne_etudiant >= 8 and moyenne_etudiant < 11:
        print("Élève moyen")
    elif moyenne_etudiant >= 0 and moyenne_etudiant < 8:
        print("Élève devant faire des efforts")
    else:
        print("Moyenne invalide")






moyenne (n,note,no)
