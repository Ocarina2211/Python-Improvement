import json



class Personnage() :
    def __init__(self, pseudo ="", classe ="", niveau = 1, vie = 100) :
        self.pseudo = pseudo
        self.classe = classe
        self.niveau = niveau
        self.vie = vie

    def __str__(self):
        return "Mon nom est " + str(self.pseudo) + ", je suis un " + str(self.classe) + ", je suis niveau " + str(self.niveau) + " et j'ai " + str(self.vie) + "PV"


    

def menu():
    print("===== RPG MANAGER =====")
    print("" \
    "")
    print("1. Créer un personnage")
    print("2. Afficher les personnages")
    print("3. Faire monter un personnage de niveau")
    print("4. Supprimer un personnage")
    print("5. Sauvegarder")
    print("6. Quitter")


joueurs = {}
menu()
while True :
    try :
        action = int(input("Quelle action voulez-ous réaliser ? : "))
        break
    except ValueError :
        print("Veuillez saisir un nombre")
        

while action != 6 :
    if action == 1 :
        nomJoueur = input("Nom du joueur : ")
        joueur = Personnage(input("Pseudo du joueur : "), input("Classe du joueur : "), 1, 100)
        joueurs[nomJoueur] = [joueur.pseudo, joueur.classe, joueur.niveau, joueur.vie]
        

    if action == 2 :
        print("" \
        "" \
        "")
        if joueurs == {} :
            print("Aucun joueur n'a été créé.")
        else :
            for joueur, infoJoueur in joueurs.items() :
                print(joueur, "== Pseudo : ", infoJoueur[0], " || Classe : ", infoJoueur[1], " || Niveau : ", infoJoueur[2], " || PV : ", infoJoueur[3])
        print("" \
        "" \
        "")

    if action == 3:
        if not joueurs:
            print("Aucun joueur n'a été créé.")
        else:
            while True:
                nom = input("Nom du joueur à améliorer (pas son pseudo) : ")

                if nom in joueurs:
                    # [pseudo, classe, niveau, vie] : le niveau est à l'indice 2.
                    joueurs[nom][2] += 1
                    print("Nouveau niveau :", joueurs[nom][2])
                    break  # Quitte la boucle de demande du nom.
                else:
                    print("Ce joueur n'existe pas. Réessaie.")

    menu()

    try :
        action = int(input("Quelle action voulez-ous réaliser ? : "))
    except  :
        print("Veuillez saisir un nombre")


print(" Au plaisir de vous revoir !")
    