class Personnage() :
    def __init__(self, nom ="", niveau = 1, vie = 100) :
        self.nom = nom
        self.niveau = niveau
        self.vie = vie

    def __str__(self):
        return "Mon nom est " + str(self.nom) + ", je suis nivveau " + str(self.niveau) + " et j'ai " + str(self.vie) + "PV"

golmon = Personnage("Golmon", 1, 100)
print(golmon)