while True :
    try :
        pseudo = str(input("Quel est ton pseudo ?"))
        niveau = str(input("Quel est ton niveau ?"))
        break
    except TypeError :
        print("Erreur, veuillez reessayer")


with open("sauvegarde.txt", "w") as fichier_sauvegarde :
     fichier_sauvegarde.write("Pseudo : " + pseudo + "\n" + 
                             "Niveau : " + niveau)