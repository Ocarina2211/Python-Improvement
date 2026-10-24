def factorielle(n) :
    if n == 0 :
        return 1
    else :
        return n*(factorielle(n - 1))


def somme_chiffres(n) :
    if n == 0 :
        return 0 
    return n + somme_chiffres(n - 1)
print(somme_chiffres(int(input("Choisir un nombre : "))))
