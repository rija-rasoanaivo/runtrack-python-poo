class Joueur():
    def __init__(self, nom, numero, position, nb_buts, nb_passe_dec, nb_cartons_jaunes, nb_cartons_rouges):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_buts = nb_buts
        self.__nb_passe_dec = nb_passe_dec
        self.__nb_cartons_jaunes = nb_cartons_jaunes
        self.__nb_cartons_rouges = nb_cartons_rouges

    def get_nom(self):
        return self.__nom
    
    def get_numero(self):
        return self.__numero
    
    def get_position(self):
        return self.__position
    
    def get_nb_buts(self):
        return self.__nb_buts
    
    def get_nb_passe_dec(self):
        return self.__nb_passe_dec
    
    def get_nb_cartons_jaunes(self):
        return self.__nb_cartons_jaunes
    
    def get_nb_cartons_rouges(self):
        return self.__nb_cartons_rouges
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_numero(self, numero):
        self.__numero = numero

    def set_position(self, position):
        self.__position = position

    def set_nb_buts(self, nb_buts):
        self.__nb_buts = nb_buts

    def set_nb_passe_dec(self, nb_passe_dec):
        self.__nb_passe_dec = nb_passe_dec

    def set_nb_cartons_jaunes(self, nb_cartons_jaunes):
        self.__nb_cartons_jaunes = nb_cartons_jaunes

    def set_nb_cartons_rouges(self, nb_cartons_rouges):
        self.__nb_cartons_rouges = nb_cartons_rouges

    def marquerUnBut(self):
        self.__nb_buts += 1

    def effectuerUnePasseDecisive(self):
        self.__nb_passe_dec += 1

    def recevoirUnCartonJaune(self):
        self.__nb_cartons_jaunes += 1

    def recevoirUnCartonRouge(self):
        self.__nb_cartons_rouges += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.__nom} :")
        print(f"    - Position : {self.__position}")
        print(f"    - Numero : {self.__numero}")
        print(f"    - Nombre de buts : {self.__nb_buts}")
        print(f"    - Nombre de passes decisives : {self.__nb_passe_dec}")
        print(f"    - Nombre de cartons jaunes : {self.__nb_cartons_jaunes}")
        print(f"    - Nombre de cartons rouges : {self.__nb_cartons_rouges}")

class Equipe():
    def __init__(self, nom_equipe, liste_joueurs=None):
        self.__nom_equipe = nom_equipe
        if liste_joueurs is None:
            liste_joueurs = []
        self.__liste_joueurs = liste_joueurs
    
    def ajouterJoueur(self, joueur):
        self.__liste_joueurs.append(joueur)
        print(f"Joueur {joueur.get_nom()} ajoute a l'equipe {self.__nom_equipe}.")

    def afficherEquipe(self):
        print(f"Equipe {self.__nom_equipe} :")
        for joueur in self.__liste_joueurs:
            print(f"    - {joueur.get_nom()} ({joueur.get_position()})")

    def AfficherStatistiques_tout_joueurs_equipe(self):
        print(f"Statistiques de l'equipe {self.__nom_equipe} :")
        for joueur in self.__liste_joueurs:
            joueur.afficherStatistiques()

    def mettreAjourStatistiqueJoueur(self, joueur, nb_buts, nb_passe_dec, nb_cartons_jaunes, nb_cartons_rouges):
        joueur.set_nb_buts(nb_buts)
        joueur.set_nb_passe_dec(nb_passe_dec)
        joueur.set_nb_cartons_jaunes(nb_cartons_jaunes)
        joueur.set_nb_cartons_rouges(nb_cartons_rouges)
        print(f"Statistiques du joueur {joueur.get_nom()} mises a jour.")

    def marquer_un_but(self, joueur):
        joueur.marquerUnBut()
        print(f"But marque par {joueur.get_nom()}.")

    def effectuer_une_passe_decisive(self, joueur):
        joueur.effectuerUnePasseDecisive()
        print(f"Passe decisive effectuee par {joueur.get_nom()}.")

    def recevoir_un_carton_jaune(self, joueur):
        joueur.recevoirUnCartonJaune()
        print(f"Carton jaune recu par {joueur.get_nom()}.")

    def recevoir_un_carton_rouge(self, joueur):
        joueur.recevoirUnCartonRouge()
        print(f"Carton rouge recu par {joueur.get_nom()}.")


Jean = Joueur("Jean", 1, "Attaquant", 0, 0, 0, 10)
Jordan = Joueur("Jordan", 9, "Ailier", 0, 3, 2, 0)
Redha = Joueur("Redha", 3, "Defenseur central", 4, 0, 0, 0)
Maxence = Joueur("Manxence", 4, "Milieur offensif", 0, 0, 0, 2)
Youcef = Joueur("Youcef", 5, "Milieu defensif", 1, 0, 0, 0)
Manon = Joueur("Manon", 6, "Arrière lateral", 0, 0, 0, 6)
Rija = Joueur("Rija", 7, "Gardien", 3, 3, 0, 0)


Ronaldo = Joueur("Ronaldo", 7, "Attaquant", 10, 0, 0, 0)
Messi = Joueur("Messi", 10, "Ailier", 5, 2, 0, 0)
Pique = Joueur("Pique", 3, "Defenseur central", 0, 0, 5, 1)
Xavi = Joueur("Xavi", 4, "Milieur offensif", 1, 2, 2, 0)
Busquets = Joueur("Busquets", 5, "Milieu defensif", 0, 1, 1, 1)
Alba = Joueur("Alba", 6, "Arrière lateral", 0, 0, 0, 0)
TerStegen = Joueur("Ter Stegen", 1, "Gardien", 0, 0, 1, 0)

Marseille = Equipe("Marseille")
Allstar = Equipe("Allstar")

Marseille.ajouterJoueur(Jean)
Marseille.ajouterJoueur(Jordan)
Marseille.ajouterJoueur(Redha)
Marseille.ajouterJoueur(Maxence)
Marseille.ajouterJoueur(Youcef)
Marseille.ajouterJoueur(Manon)
Marseille.ajouterJoueur(Rija)

Marseille.afficherEquipe()

Allstar.ajouterJoueur(Ronaldo)
Allstar.ajouterJoueur(Messi)
Allstar.ajouterJoueur(Pique)
Allstar.ajouterJoueur(Xavi)
Allstar.ajouterJoueur(Busquets)
Allstar.ajouterJoueur(Alba)
Allstar.ajouterJoueur(TerStegen)

Allstar.afficherEquipe()

Marseille.AfficherStatistiques_tout_joueurs_equipe()
Allstar.AfficherStatistiques_tout_joueurs_equipe()

Allstar.marquer_un_but(Ronaldo)

Allstar.effectuer_une_passe_decisive(Messi)

Allstar.recevoir_un_carton_jaune(Pique)

Allstar.recevoir_un_carton_rouge(Pique)

Allstar.AfficherStatistiques_tout_joueurs_equipe()





