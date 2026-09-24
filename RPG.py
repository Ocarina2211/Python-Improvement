class Personnage :

    def __init__(self, nom, vie , attaque, niveau ):
        self.nom = nom
        self.vie = vie 
        self.attaque = attaque 
        self.niveau = niveau


joueur = Personnage("Matthieu", 100, 20, 1)
print(joueur.nom)