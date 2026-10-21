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


liste = []
menu()

try :
    action = int(input("Quelle action voulez-ous réaliser ? : "))
except  :
    print("Veuillez saisir un nombre")

while action != 6 :
    if action == 1 :
        a = input("NomPerso :")
        a  = Personnage(input("Pseudo : "), input("Classe : "), 1 ,100)
        liste.append(str(a))
        print("Personnage créé !")

    if action == 2 :
        print("" \
        "" \
        "")
        for joueur in liste :
            print(joueur)
        print("" \
        "" \
        "")

    if action == 3 :
        pass


    menu()

    try :
        action = int(input("Quelle action voulez-ous réaliser ? : "))
    except  :
        print("Veuillez saisir un nombre")


print(" Au plaisir de vous revoir !")
    