class Personnage :

    def __init__(self, nom, vie , attaque, niveau, vie_max ):
        self.nom = nom
        self.vie = vie 
        self.attaque = attaque 
        self.niveau = niveau
        self.vie_max = vie_max


    def presenter(self):
        print("Je suis", self.nom)
        if self.vie > 0 :
            print("J'ai", self.vie,"PV")
        else :
            print("Je suis mort")
        print("Mes attaques font", self.attaque, "dégats")
        print("Je suis niveau", self.niveau)


    def recevoir_degats(self, degats):
        if self.vie > degats :
            self.vie -= degats
        else :
            self.vie = 0


    def attaquer(self, cible):
        cible.recevoir_degats(self.attaque)


    def heal(self, heal):
        if self.vie + heal <= self.vie_max :
            print("PV Avant Heal : ", self.vie)
            self.vie += heal
            print("PV actuel : ", self.vie)
            print("Power heal :", heal)
        else :
            print("PV Avant Heal : ", self.vie)
            self.vie = self.vie_max
            print("PV actuel : ", self.vie)
            print("Power heal :", heal)




class Guerrier(Personnage):
    def __init__(self, nom, vie, attaque, niveau, vie_max, shield):
        super().__init__(nom, vie, attaque, niveau, vie_max)
        self.shield = shield

    def presenter(self):
        super().presenter()
        if self.shield > 0 :
            print("J'ai",self.shield, " de shield")
        else :
            print ("J'ai plus de shield")


    def recevoir_degats(self, degats):
        if self.shield > 0:
            degats = degats / 2
            self.shield -= degats

        if self.shield < 0:
            self.shield = 0

        super().recevoir_degats(degats)

    



class Mage(Personnage):
    def __init__(self, nom, vie, attaque, niveau, vie_max, mana):
        super().__init__(nom, vie, attaque, niveau, vie_max)
        self.mana = mana

    def presenter(self):
        super().presenter()
        print("J'ai", self.mana, " de mana ")
   
def combat(joueur1, joueur2):
    tour = 1
    while joueur1.vie > 0 and joueur2.vie > 0 :
        print(" --- TOUR ",tour, "---")
        print("" \
        "")
        joueur1.attaquer(joueur2)
        print("" \
        "")
        if joueur2.vie > 0 :
            joueur2.attaquer(joueur1)
        print("" \
        "")
        tour += 1
    if joueur1.vie == 0 :
        print(joueur2.nom, "a détruit", joueur1.nom,"!!!")
    else :
        print(joueur1.nom, "a détruit", joueur2.nom,"!!!")
    
        

joueur1 = Personnage("Matthieu", 100, 20, 1, 100)
ennemi1 = Personnage("Goblin", 100, 30, 1, 100)
guerrier = Guerrier("Brutus", 100, 40, 1, 130, 25 )
harry = Mage("Harry", 100, 20, 1, 100, 70)


guerrier.presenter()
harry.attaquer(guerrier)
guerrier.presenter()
