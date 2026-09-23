date = ("samedi", 21, 10, 1995)
jours = [
    "lundi",
    "mardi",
    "mercredi",
    "jeudi",
    "vendredi",
    "samedi",
    "dimanche",
]
mois = {
    1: ("janvier", 31),
    2: ("février", 28),
    3: ("mars", 31),
    4: ("avril", 30),
    5: ("mai", 31),
    6: ("juin", 30),
    7: ("juillet", 31),
    8: ("août", 31),
    9: ("septembre", 30),
    10: ("octobre", 31),
    11: ("novembre", 30),
    12: ("décembre", 31),
}
def jour_suivant(date):
    nom_jour, num_jour, num_mois, num_annee = date

    index_jour = jours.index(nom_jour)
    nom_jour = jours[(index_jour + 1) % len(jours)]

    nombre_de_jours = mois[num_mois][1]

    if num_jour < nombre_de_jours:
        num_jour += 1
    else:
        num_jour = 1
        if num_mois == 12:
            num_mois = 1
            num_annee += 1
        else:
            num_mois += 1

    return (nom_jour, num_jour, num_mois, num_annee)

print(jour_suivant(date))
