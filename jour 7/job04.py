def decaler(message ,decalage):
    resultat= ""

    for lettre in message :
        if lettre.isalpha() and lettre.isascii():
            base =ord ("A") if lettre.isupper() else ord ("a")
            nouvelle_lettre = chr((ord(lettre) - base + decalage) % 26 + base)
            resultat+= nouvelle_lettre 
        else : 
            resultat+= lettre 

    return resultat

print (decaler("bonjour",3))