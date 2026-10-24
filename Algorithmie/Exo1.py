joueurs = ["Lucas", "Hugo", "Matthieu", "Arthur", "Teva"]
pseudo = input("Quel pseudo veut tu rechercher ? : ")
tour = 0
trouve = False
for joueur in joueurs :
    tour +=1
    if joueur == pseudo :
        trouve = True
        break

if trouve == True :
    print(f"Joueur Trouvé ! Il a fallu {tour} comparaisons")
else :
    print(f"Joueur introuvable après {tour} comparaisons")
        