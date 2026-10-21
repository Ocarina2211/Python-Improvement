import json

donnees = []
nbr_joueurs = 3
n = 0

while n < nbr_joueurs :
    pseudo = input("Pseudo : ")
    niveau = int(input("Niveau : "))
    pv = int(input("PV : "))
    joueur = {"Pseudo" : pseudo, "Niveau" : niveau, "PV" : pv}
    donnees.append(joueur)
    n += 1

with open ("sauvegarde.json", "w") as fichier:
    json.dump(donnees, fichier, indent=4)

with open ("sauvegarde.json", "r") as fichier :
    infos = json.load(fichier)
    for info in infos :
        print("Le pseudo est ", info["Pseudo"], "et il est niveau", info["Niveau"])
        print()

        