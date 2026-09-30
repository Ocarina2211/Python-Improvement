while True :
    try :
        pseudo = str(input("Quel est ton pseudo ?"))
        niveau = int(input("Quel est ton niveau ?"))
        break
    except ValueError :
        print("Erreur, veuillez rentrer un nombre")


with open("sauvegarde.txt", "w") as fichier_sauvegarde :
     fichier_sauvegarde.write("Pseudo : " + pseudo + "\n" + 
                             "Niveau : " + str(niveau))

with open("sauvegarde.txt", "r") as fichier_sauvegarde :
    contenu = fichier_sauvegarde.read()
    #print(contenu)

with open("sauvegarde.txt", "r") as fichier_sauvegarde :
    liste = fichier_sauvegarde.readlines()
    print(liste)
    pseudo = liste[0].split(" : ")
    detail = pseudo[1].split("\n")
    niveau = liste[1].split(" : ")
    pseudo_charge = detail[0]
    niveau_charge = int(niveau[1])
    print(pseudo_charge)
    print(niveau_charge)