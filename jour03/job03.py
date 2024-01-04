class Tache:
    def __init__(self, titre, description):
        self.__titre = titre
        self.__description = description
        self.__statut = "A faire" or "Terminé"

    def get_titre(self):
        return self.__titre
    
    def get_description(self):
        return self.__description
    
    def get_statut(self):
        return self.__statut
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_description(self, description):
        self.__description = description

    def set_statut(self, statut):
        self.__statut = statut

class ListeDeTaches:
    def __init__(self, nom):
        self.__nom = nom
        self.__taches = []

    def get_nom(self):
        return self.__nom
    
    def get_taches(self):
        return self.__taches
    
    def set_nom(self, nom):
        self.__nom = nom

    def set_taches(self, taches):
        self.__taches = taches

    def ajouter_tache(self, tache):
        self.__taches.append(tache)
        print(f"Tache ajoutee a la liste de taches {self.__nom} : {tache.get_titre()}")
    
    def supprimer_tache(self, tache):
        self.__taches.remove(tache)
        print(f"Tache supprimee de la liste de taches {self.__nom} : {tache.get_titre()}")
    
    def afficher_liste(self):
        print(f"Liste de taches {self.__nom} :")
        for tache in self.__taches:
            print(f"    - {tache.get_titre()} : {tache.get_description()} ({tache.get_statut()})")
    
    def marquer_comme_terminee(self, tache):
        tache.set_statut("Terminé")
        print(f"Tache {tache.get_titre()} marquee comme terminee.")

    def filtrer_liste(self, statut):
        print(f"Liste de taches {self.__nom} :")
        for tache in self.__taches:
            if tache.get_statut() == statut:
                print(f"    - {tache.get_titre()} : {tache.get_description()} ({tache.get_statut()})")


tache1 = Tache("Faire les courses", "Acheter du pain, du lait et des oeufs.")
tache2 = Tache("Faire la vaisselle", "Laver les assiettes, les couverts et les verres.")
tache3 = Tache("Faire le menage", "Passer l'aspirateur, laver le sol et nettoyer les vitres.")


liste_de_taches1 = ListeDeTaches("de Rija")
liste_de_taches1.ajouter_tache(tache1)
liste_de_taches1.ajouter_tache(tache2)
liste_de_taches1.ajouter_tache(tache3)
liste_de_taches1.afficher_liste()
liste_de_taches1.marquer_comme_terminee(tache1)
liste_de_taches1.afficher_liste()
liste_de_taches1.filtrer_liste("A faire")

tache4 = Tache("Faire la lessive", "Laver les vetements et les etendre.")
tache5 = Tache("Faire la cuisine", "Preparer le repas du soir.")
tache6 = Tache("Promener le chien", "Sortir le chien pour qu'il fasse ses besoins.")

liste_de_taches2 = ListeDeTaches("de Manon")
liste_de_taches2.ajouter_tache(tache4)
liste_de_taches2.ajouter_tache(tache5)
liste_de_taches2.ajouter_tache(tache6)
liste_de_taches2.afficher_liste()
liste_de_taches2.marquer_comme_terminee(tache6)
liste_de_taches2.afficher_liste()
liste_de_taches2.filtrer_liste("Terminé")