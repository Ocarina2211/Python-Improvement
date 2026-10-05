import json

ps = str((input("Choisi ton pseudo")))
nv = int(input("Choisi ton niveau"))
pv = int(input("Choisi tes pv"))

joueur = {"Pseudo" : ps, "Niveau" : nv, "PV" : pv}

with open("sauvegarde.json", "w") as fichier:
    json.dump(joueur, fichier, indent=4)