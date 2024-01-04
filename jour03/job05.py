import random

class Personnage:
    def __init__(self, nom):
        self.__nom = nom
        self.__vie = 30
    
    def get_nom(self):
        return self.__nom
    
    def get_vie(self):
        return self.__vie
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_vie(self, vie):
        self.__vie = vie

    def attaquer(self, personnage):
        personnage.set_vie(personnage.get_vie() - 1)
        print(f"{self.__nom} attaque {personnage.get_nom()} !")
        print(f"{personnage.get_nom()} a maintenant {personnage.get_vie()} points de vie.")

class Jeu:
    def __init__(self):
        self.__personnages = []
        self.niveau = ""

    def choisirNiveau(self):
        self.niveau = input("Choisissez un niveau de difficulte (facile, moyen ou difficile) : ")
        print(f"Vous avez choisi le niveau {self.niveau}.")
        if self.niveau == "facile":
            self.vie = 30
        elif self.niveau == "moyen":
            self.vie = 20
        elif self.niveau == "difficile":
            self.vie = 10
        else:
            print("Niveau invalide.")
            self.choisirNiveau()

    def lancerJeu(self):
        self.choisirNiveau()
        self.joueur = Personnage(input("Choisissez un nom pour votre personnage : "))
        self.ennemi = Personnage(input("Choisissez un nom pour votre ennemi : "))
        self.joueur.set_vie(self.vie)
        self.ennemi.set_vie(self.vie)
        self.__personnages.append(self.joueur)
        self.__personnages.append(self.ennemi)
    
    # def deroulementJeu(self):
    #     while self.joueur.get_vie() > 0 and self.ennemi.get_vie() > 0:
    #         self.joueur.attaquer(self.ennemi)
    #         self.ennemi.attaquer(self.joueur)
    #     if self.joueur.get_vie() <= 0:
    #         print(f"{self.joueur.get_nom()} a perdu !")
    #     elif self.ennemi.get_vie() <= 0:
    #         print(f"{self.ennemi.get_nom()} a perdu !")
        
    def deroulementJeualeatoire(self):
        while self.joueur.get_vie() > 0 and self.ennemi.get_vie() > 0:
            random.choice(self.__personnages).attaquer(random.choice(self.__personnages))
        if self.joueur.get_vie() <= 0:
            print(f"{self.joueur.get_nom()} a perdu !")
        elif self.ennemi.get_vie() <= 0:
            print(f"{self.ennemi.get_nom()} a perdu !")


jeu = Jeu()

jeu.lancerJeu()
# jeu.deroulementJeu()
jeu.deroulementJeualeatoire()