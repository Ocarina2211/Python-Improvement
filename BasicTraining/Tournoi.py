joueurs = {
    "Matthieu": {"victoires": 7, "defaites": 3, "points": 850},
    "Lucas": {"victoires": 4, "defaites": 6, "points": 620},
    "Emma": {"victoires": 9, "defaites": 1, "points": 1100},
    "Nathan": {"victoires": 5, "defaites": 5, "points": 740},
    "Chloe": {"victoires": 8, "defaites": 2, "points": 970}
}


def calculer_taux(joueurs):
    dic = {} 
    for nom, stats in joueurs.items():
        dic[nom] = str(stats["victoires"]) + " V",str(stats["defaites"]) + " D", str(stats["points"]) + " points",str((stats["victoires"] / (stats["victoires"] + stats["defaites"]) * 100)) + " % de victoires"
    return dic


def find_meilleur_joueur(joueurs):
    meilleur_score = 0
    meilleur_joueur = ""
    for nom, stats in joueurs.items():
        if stats["points"] > meilleur_score:
            meilleur_score = stats["points"]
            meilleur_joueur = nom
    return meilleur_joueur

def calcul_moyenne_points(joueurs):
    moyenne = 0
    somme = 0
    n = 0
    for stats in joueurs.values():
        somme += stats["points"]
        n += 1
    moyenne = somme / n
    return moyenne

def calcul_nbr_pers_avec_50_pourcents_winrate(joueurs):
    somme = 0
    for stats in joueurs.values():
        if (stats["victoires"] / (stats["victoires"] + stats["defaites"]) * 100) > 50:
            somme += 1
    return somme


print("=== TOURNOI ===")

print("" \
"" \
"")
for nom, stats in calculer_taux(joueurs).items():
    print(nom, " : ",stats[0], " /", stats[1], " - ", stats[2], "-", stats[3])

print("" \
"" \
"")

print("Meilleur joueur : ", find_meilleur_joueur(joueurs))
print("Moyenne des points : ", calcul_moyenne_points(joueurs))
print("Joueur avec plus de 50% winrate : ", calcul_nbr_pers_avec_50_pourcents_winrate(joueurs))

print("" \
"" \
"")