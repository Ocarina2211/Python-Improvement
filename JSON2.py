import json

try :
    with open ("joueurs.json", "r") as fichier :
        infos = json.load(fichier)
        for info in infos :
                print("Le pseudo est ", info["Pseudo"], "et il est niveau", info["Niveau"])
                print()
except FileNotFoundError:
    print("Aucune sauvegarde trouvée")