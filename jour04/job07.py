import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def getValeur(self):
        return self.valeur

    def getCouleur(self):
        return self.couleur

    def valeurCarte(self):
        if self.valeur.isdigit():
            return int(self.valeur)
        elif self.valeur == "Deux":
            return 2
        elif self.valeur == "Trois":
            return 3
        elif self.valeur == "Quatre":
            return 4
        elif self.valeur == "Cinq":
            return 5
        elif self.valeur == "Six":
            return 6
        elif self.valeur == "Sept":
            return 7
        elif self.valeur == "Huit":
            return 8
        elif self.valeur == "Neuf":
            return 9
        elif self.valeur in ("Roi", "Dame", "Valet"):
            return 10
        elif self.valeur == "As":
            choix = int(input("Choisissez la valeur de l'As (1 ou 11) : "))
            while choix not in (1, 11):
                choix = int(input("Choisissez la valeur de l'As (1 ou 11) : "))
            return choix
        else:
            return 0

class Jeu:
    def __init__(self):# Création du paquet de cartes
        self.valeurs = ["As", "Deux", "Trois", "Quatre", "Cinq", "Six", "Sept", "Huit", "Neuf", "Dix", "Roi", "Dame", "Valet"]
        self.couleurs = ["Pique", "Coeur", "Carreau", "Trefle"]
        self.paquet = []

    def creationPaquet(self): # Création du paquet de cartes    
        self.paquet = [Carte(valeur, couleur) for valeur in self.valeurs for couleur in self.couleurs] #for valeur in self.valeurs for couleur in self.couleurs signifie que pour chaque valeur, on va créer une carte pour chaque couleur 

    def melangerPaquet(self): # Mélange du paquet de cartes
        random.shuffle(self.paquet) #random.shuffle permet de mélanger le paquet de cartes

    def tirerCarte(self): # Tirer une carte du paquet
        if self.paquet:
            return self.paquet.pop() #pop permet de retirer la dernière carte du paquet
        else:
            return "Plus de cartes dans le paquet"

    def afficherMain(self, main): # Afficher la main du joueur
        for carte in main:
            print(carte.getValeur(), "de", carte.getCouleur())

    def scoreMain(self, main): # Calculer le score de la main du joueur
        score = 0
        as_compte = sum(1 for carte in main if carte.getValeur() == "As")

        for carte in main:
            score += carte.valeurCarte()

        while as_compte > 0 and score + 10 <= 21:
            score += 10
            as_compte -= 1

        return score

    def partie(self):
        self.creationPaquet()
        self.melangerPaquet()
        main_joueur = [self.tirerCarte() for _ in range(2)] #for _ in range(2) signifie que l'on va tirer 2 cartes
        main_croupier = [self.tirerCarte() for _ in range(2)] #for _ in range(2) signifie que l'on va tirer 2 cartes

        print("Main du joueur :")
        self.afficherMain(main_joueur)
        print("Score :", self.scoreMain(main_joueur))

        print("Main du croupier :")
        self.afficherMain(main_croupier)
        print("Score :", self.scoreMain(main_croupier))

        while self.scoreMain(main_joueur) < 21:
            choix = input("Voulez-vous tirer une carte ? (o/n) ")
            if choix == "o":
                main_joueur.append(self.tirerCarte())
                print("Main du joueur :")
                self.afficherMain(main_joueur)
                print("Score :", self.scoreMain(main_joueur))
            else:
                break

        if self.scoreMain(main_joueur) > 21:
            print("Vous avez perdu")
        else:
            while self.scoreMain(main_croupier) < 17:
                main_croupier.append(self.tirerCarte())

            print("Main du croupier :")
            self.afficherMain(main_croupier)
            print("Score :", self.scoreMain(main_croupier))

            if self.scoreMain(main_croupier) > 21:
                print("Vous avez gagné")
            elif self.scoreMain(main_joueur) > self.scoreMain(main_croupier):
                print("Vous avez gagné")
            else:
                print("Vous avez perdu")

        choix = input("Voulez-vous rejouer ? (o/n) ")
        if choix == "o":
            self.partie()

# Pour commencer une partie
jeu = Jeu()
jeu.partie()