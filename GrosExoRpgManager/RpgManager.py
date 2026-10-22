
import json


class Personnage:
    def __init__(self, pseudo=None, classe=None, niveau=1, vie=100):
        self.pseudo = pseudo
        self.classe = classe
        self.niveau = niveau
        self.vie = vie

    def __str__(self):
        return (f"Mon nom est {self.pseudo}, je suis un {self.classe}, "
                f"je suis niveau {self.niveau} et j'ai {self.vie} PV")


def menu():
    print("\n===== RPG MANAGER =====")
    print("1. Créer un personnage")
    print("2. Afficher les personnages")
    print("3. Faire monter un personnage de niveau")
    print("4. Supprimer un personnage")
    print("5. Sauvegarder")
    print("6. Quitter")

    while True:
        try:
            action = int(input("Quelle action voulez-vous réaliser ? : "))

            if 1 <= action <= 6:
                return action

            print("Veuillez choisir un nombre entre 1 et 6.")

        except ValueError:
            print("Veuillez saisir un nombre valide.")


# Chargement des personnages
try:
    with open("personnages.json", "r", encoding="utf-8") as fichier:
        joueurs = json.load(fichier)

except FileNotFoundError:
    joueurs = {}


# Boucle principale
while True:
    action = menu()

    if action == 1:
        nom_joueur = input("Nom du joueur : ")

        joueur = Personnage(
            input("Pseudo du joueur : "),
            input("Classe du joueur : ")
        )

        joueurs[nom_joueur] = [
            joueur.pseudo,
            joueur.classe,
            joueur.niveau,
            joueur.vie
        ]

        print("Personnage créé avec succès !")

    elif action == 2:
        print("\n=== PERSONNAGES ===")

        if not joueurs:
            print("Aucun personnage n'existe.")
        else:
            for nom, infos in joueurs.items():
                print(
                    f"{nom} == Pseudo : {infos[0]} || "
                    f"Classe : {infos[1]} || "
                    f"Niveau : {infos[2]} || PV : {infos[3]}"
                )

    elif action == 3:
        print("\n=== AMÉLIORATION DE NIVEAU ===")

        if not joueurs:
            print("Aucun joueur n'a été créé.")
        else:
            pseudo = input("Pseudo du personnage : ")
            trouve = False

            for infos in joueurs.values():
                if infos[0] == pseudo:
                    infos[2] += 1
                    trouve = True
                    print(f"{pseudo} passe au niveau {infos[2]} !")
                    break

            if not trouve:
                print("Joueur introuvable.")

    elif action == 4:
        print("\n=== SUPPRESSION DE PERSONNAGE ===")

        if not joueurs:
            print("Aucun joueur n'a été créé.")
        else:
            pseudo = input("Pseudo du personnage à supprimer : ")
            cle_a_supprimer = None

            for nom, infos in joueurs.items():
                if infos[0] == pseudo:
                    cle_a_supprimer = nom
                    break

            if cle_a_supprimer is not None:
                del joueurs[cle_a_supprimer]
                print(f"{pseudo} a été supprimé !")
            else:
                print("Joueur introuvable.")

    elif action == 5:
        with open("personnages.json", "w", encoding="utf-8") as fichier:
            json.dump(joueurs, fichier, indent=4, ensure_ascii=False)

        print("Tous vos personnages ont été sauvegardés !")

    elif action == 6:
        print("Au plaisir de vous revoir !")
        break
