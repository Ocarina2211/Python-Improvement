comptes = {
    "Matthieu": 1250,
    "Lucas": 850,
    "Emma": 2100
}

def afficher_les_comptes(comptes):
    print("=== COMPTES ===")
    print("" \
    "")
    for nom, argent in comptes.items():
        print(nom, ":",argent, "€")


def depot_argent(comptes):
    compte = str(input("Quel est tom nom ? "))
    if compte in comptes.keys():
        ancien_montant = comptes[compte]
        montant = float(input("Combien souhaitez-vous déposer sur votre compte ?"))
        if montant > 0 :
            comptes[compte] = ancien_montant + montant
            print("Depot réussi ! ")
            print("Votre compte est passé de ", ancien_montant, "€ à",comptes[compte], "€")
        else :
            print("Vous devez saisir une valeur supérieur à 0")
    else :
        print("Nous n'avons pas de compte à votre nom, veuillez réssayer")

def retirer_argent(comptes):
    compte = str(input("Quel est tom nom ? "))
    if compte in comptes.keys():
        ancien_montant = comptes[compte]
        montant = float(input("Combien souhaitez-vous retirer sur votre compte ?"))
        if montant > 0 and montant < ancien_montant :
            comptes[compte] = ancien_montant - montant
            print("Action réussi ! ")
            print("Votre compte est passé de ", ancien_montant, "€ à",comptes[compte], "€")

        else :
            print("Vous devez saisir une valeur supérieur à 0")

    else :
         print("Nous n'avons pas de compte à votre nom, veuillez réssayer")



def virement(comptes):
    accSource =str(input("Choisir le compte source : "))
    if accSource in comptes:
        accDest = str(input("Choisir le compte destinataire : "))
        if accDest in comptes :
            montant = float(input("Combien souhaitez vous transférer ?"))
            if montant > 0 and montant < comptes[accSource]:
                comptes[accSource] -= montant
                comptes[accDest] += montant
                print("" \
                "" \
                "")
                print("Compte source : ",accSource)
                print("Compte destinataire : ", accDest)
                print("Montant : ", montant)
                print("" \
                "")
                print("Virement effectué !")
                print("" \
                "")
                print(accSource, " : ", comptes[accSource],"€")
                print(accDest, " :", comptes[accDest], "€")

            elif montant < 0 :
                print("Veuillez saisir un montant supérieur à 0")
            else:
                print("Vous n'avez pas cette somme sur votre compte.")

        else :
            print("Ce nom n'est pas enregistré dans notre banque")
    else :
        print("Ce nom n'est pas enregistré dans notre banque")

virement(comptes)