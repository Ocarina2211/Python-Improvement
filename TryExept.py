while True :
    try :
        premier_nbr = int(input("Choisis un numérateur"))
        deuxieme_nbr = int(input("Choisis un dénominateur"))
        resultat = premier_nbr / deuxieme_nbr
        break
    except ValueError :
        print("Tu dois écrire le nombre en chiffres pas en lettres")
    except ZeroDivisionError :
        print("Tu ne peux pas diviser un nombre par zéro")

    

print("Mon numérateur est :", premier_nbr)
print("Mon dénominateur est :", deuxieme_nbr)
print("Le Résultat de la division est : ", resultat)
