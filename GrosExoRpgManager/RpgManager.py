import json



class Personnage() :
    def __init__(self, pseudo =None, classe =None, niveau = 1, vie = 100) :
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
        action = int(input("Quelle action voulez-vous réaliser ? : "))
        break
    except ValueError :
        print("Veuillez saisir un nombre")
        

while action != 6 : # Quitter
    if action == 1 : # Créer un personnage
        nomJoueur = input("Nom du joueur : ")
        joueur = Personnage(input("Pseudo du joueur : "), input("Classe du joueur : "), 1, 100)
        joueurs[nomJoueur] = [joueur.pseudo, joueur.classe, joueur.niveau, joueur.vie]
        

    if action == 2 : # Afficher les personnages
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

    if action == 3: # Ajouter un niveau à un joueur
        print("\n=== Amélioration de niveau ===\n")
        if not joueurs:
            print("Aucun joueur n'a été créé.")
        else:
            while True:
                ps = input("Qui recevra l'augmentation de niveau ? : ")
                for nomJoueur, infoJoueur in joueurs.items():
                    if infoJoueur[0] == ps :
                        infoJoueur[2] += 1
                        print("L'augmentation de niveau de", infoJoueur[0]," a été réalisé avec succès !")
                    else :
                        print("Aucun joueur n'a ce pseudo")
                break

    if action == 4: # Supprimer un joueur
        print("\n=== Suppression de personnage ===\n")
        if not joueurs :
            print("Aucun joueur n'a été créé.")
        else :
            while True :
                ps = input("Veuillez saisir le pseudo du joueur que vous souhaiter supprimer : ")
                for nomJoueur, infoJoueur in joueurs.items():
                    if infoJoueur[0] == ps :
                        print("Le joueur", infoJoueur[0], " a été supprimé avec succès ! ")
                        del joueurs[nomJoueur]
                    else :
                        print("Aucun joueur n'a ce pseudo")
                break 
                        

                

    menu()

    try :
        action = int(input("Quelle action voulez-ous réaliser ? : "))
    except  :
        print("Veuillez saisir un nombre")


print(" Au plaisir de vous revoir !")
    