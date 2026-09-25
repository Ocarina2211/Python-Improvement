class Personnage :

    def __init__(self, nom, vie , attaque, niveau, vie_max ):
        self.nom = nom
        self.vie = vie 
        self.attaque = attaque 
        self.niveau = niveau
        self.vie_max = vie_max

    def presenter(self):
        print("Je suis", self.nom)
        print("J'ai", self.vie,"PV")
        print("Mes attaques font", self.attaque, "dégats")
        print("Je suis niveau", self.niveau)

    def attaquer(self, cible):
        cible.vie -= self.attaque
        print(self.nom, "attaque", cible.nom, "!!! Il lui infligeant", self.attaque, "dégats")
        if cible.vie <= 0 :
            print(cible.nom, "est mort, la honte")
            cible.vie = 0

    def heal(self, heal):
        if self.vie + heal <= self.vie_max :
            print("PV Avant Heal : ", self.vie)
            self.vie += heal
            print("PV actuel : ", self.vie)
            print("Power heal :", heal)
        else :
            print("PV Avant Heal : ", self.vie)
            self.vie = 100
            print("PV actuel : ", self.vie)
            print("Power heal :", heal)
        
   
def combat(joueur1, joueur2):
    while joueur1.vie > 0 or joueur2.vie > 0 :
        tour = 1
        print(" --- TOUR ",tour, "---")
        

joueur1 = Personnage("Matthieu", 100, 50, 1, 100)
ennemi1 = Personnage("Goblin", 100, 30, 1, 100)


