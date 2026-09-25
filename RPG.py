class Personnage :

    def __init__(self, nom, vie , attaque, niveau ):
        self.nom = nom
        self.vie = vie 
        self.attaque = attaque 
        self.niveau = niveau

    def presenter(self):
        print("Je suis", self.nom)
        print("J'ai", self.vie,"PV")
        print("Mes attaques font ", self.attaque, "dégats")
        print("Je suis niveau", self.niveau)

    def attaquer(self, cible):
        cible.vie -= self.attaque
        if cible.vie <= 0 :
            print(cible.nom, "est mort, la honte")
        
   


joueur1 = Personnage("Matthieu", 100, 20, 1)
ennemi1 = Personnage("Goblin", 100, 30, 1)
joueur1.presenter()
joueur1.attaquer(ennemi1)
ennemi1.presenter()