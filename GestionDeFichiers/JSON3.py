import json

with open ("joueurs.json", "r") as fichier :
    donnees =json.load(fichier)
    find = False
    ps = input("Quel est votre pseudo ? : ")
    for player in donnees :
        if player["Pseudo"] == ps :
            player["Niveau"] += 1
            find = True
            print("Niveau de ", player["Pseudo"], "augmenté !")
    if not find :
        print("Joueur introuvable")

with open ("joueurs.json", "w") as fichier :
    json.dump(donnees, fichier, indent=4)

        
    