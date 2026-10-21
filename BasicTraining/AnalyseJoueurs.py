joueurs = {
    "Alex": [12, 18, 9, 15, 20],
    "Lina": [20, 17, 19, 18],
    "Tom": [8, 11, 14, 10, 7],
    "Sarah": [15, 15, 16, 14, 15]
}



def analyser_joueurs(joueurs):

    mega = {}
    victoire = 18

    for nom, notes in joueurs.items():
        resultat = {}
        somme = 0
        max = 0
        sommeVictoire = 0

        for note in notes :
            somme += note
            moyenne = somme / len(joueurs[nom])

            if note > max:
                max = note

            if note >= victoire :
                sommeVictoire += 1

        resultat["Moyenne"] = moyenne
        resultat["Meilleur score"] = max
        resultat["nb_victoire"] = sommeVictoire
        mega[nom] = resultat

    return mega


resultat = analyser_joueurs(joueurs)


def classer_joueurs(resultat):
    liste = []
    for nom in resultat :
        liste.append((nom,resultat[nom]["Moyenne"]))
    liste.sort(key=lambda x: x[1], reverse=True)
    return liste

classement = classer_joueurs(resultat)
print(classement)

