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
        print(self.nom, "attaque", cible.nom, "!!!")
        if cible.vie <= 0 :
            print(cible.nom, "est mort, la honte")
            cible.vie = 0
        print(cible.nom, " : ",cible.vie,"/",cible.vie_max, "PV")

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


combat(joueur1, ennemi1)

