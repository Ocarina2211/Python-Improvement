comptes = {
    "Matthieu": 1250,
    "Lucas": 850,
    "Emma": 2100
}


def afficher_comptes():
    print("\n=== COMPTES ===")
    for nom, solde in comptes.items():
        print(f"{nom} : {solde} €")


def deposer_argent():
    nom = input("Sur quel compte voulez-vous déposer ? ")

    if nom not in comptes:
        print("Ce compte n'existe pas.")
        return

    montant = float(input("Montant à déposer : "))

    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
        return

    comptes[nom] += montant
    print(f"Dépôt de {montant} € effectué sur le compte de {nom}.")


def retirer_argent():
    nom = input("Sur quel compte voulez-vous retirer ? ")

    if nom not in comptes:
        print("Ce compte n'existe pas.")
        return

    montant = float(input("Montant à retirer : "))

    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
        return

    if montant > comptes[nom]:
        print("Solde insuffisant.")
        return

    comptes[nom] -= montant
    print(f"Retrait de {montant} € effectué.")


def faire_virement():
    source = input("Compte source : ")
    destination = input("Compte destinataire : ")

    if source not in comptes:
        print("Le compte source n'existe pas.")
        return

    if destination not in comptes:
        print("Le compte destinataire n'existe pas.")
        return

    if source == destination:
        print("Impossible de faire un virement vers le même compte.")
        return

    montant = float(input("Montant du virement : "))

    if montant <= 0:
        print("Le montant doit être supérieur à 0.")
        return

    if montant > comptes[source]:
        print("Solde insuffisant.")
        return

    comptes[source] -= montant
    comptes[destination] += montant

    print(f"Virement de {montant} € effectué de {source} vers {destination}.")


def afficher_plus_riche():
    meilleur_nom = ""
    meilleur_solde = -1

    for nom, solde in comptes.items():
        if solde > meilleur_solde:
            meilleur_solde = solde
            meilleur_nom = nom

    print(f"Compte le plus riche : {meilleur_nom} avec {meilleur_solde} €")


def afficher_menu():
    print("\n=== BANQUE ===")
    print("1 - Afficher les comptes")
    print("2 - Déposer de l'argent")
    print("3 - Retirer de l'argent")
    print("4 - Faire un virement")
    print("5 - Afficher le compte le plus riche")
    print("6 - Quitter")


def programme():
    continuer = True

    while continuer:
        afficher_menu()
        choix = input("Choix : ")

        if choix == "1":
            afficher_comptes()

        elif choix == "2":
            deposer_argent()

        elif choix == "3":
            retirer_argent()

        elif choix == "4":
            faire_virement()

        elif choix == "5":
            afficher_plus_riche()

        elif choix == "6":
            continuer = False
            print("Au revoir !")

        else:
            print("Choix invalide.")


programme()