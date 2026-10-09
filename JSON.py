import json

ps = (input("Choisi ton pseudo"))
nv = int(input("Choisi ton niveau"))
pv = int(input("Choisi tes pv"))

joueur = {"Pseudo" : ps, "Niveau" : nv, "PV" : pv}

with open("sauvegarde.json", "w") as fichier:
    json.dump(joueur, fichier, indent =  4)

with open("sauvegarde.json", "r") as fichier:
    joueur = json.load(fichier)
    print("=== JOUEUR CHARGÉ ===")
    print("Pseudo :", joueur["Pseudo"])
    print("Niveau :", joueur["Niveau"])
    print("PV :", joueur["PV"])