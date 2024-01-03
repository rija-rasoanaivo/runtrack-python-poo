class Commande:
    def __init__(self, numero_commande, liste_plats_commandes, statut_commande):
    
        self.__numero_commande = numero_commande
        self.__liste_plats_commandes = liste_plats_commandes
        self.__statut_commande = statut_commande
        self.plat = {
            "Pizza": 10.2,
            "Pates": 8, 
            "Frites": 5,
            "Salade": 3,
            }
    
    def ajout_plat_au_menu(self, plat, prix):
        if plat in self.plat:
            print("Ce plat est déjà dans le menu.")
        else:
            self.plat[plat] = prix
            print(f"Le plat {plat} a été ajouté au menu.")

    def ajout_plat(self, plat):
        self.__liste_plats_commandes.append(plat)
        print(f"Le plat {plat} a été ajouté à la commande.")

    def set_annulation_commande(self):
        self.__statut_commande = "Annulée"
        self.__liste_plats_commandes = []
        print("La commande a été annulée.")

    def get_numero_commande(self):
        print(f"Le numéro de la commande est : {self.__numero_commande}")
        return self.__numero_commande
    
    def get_liste_plats_commandes(self):
        print(f"Les plats commandés sont : {self.__liste_plats_commandes}")
        return self.__liste_plats_commandes
    
    def get_statut_commande(self):
        return self.__statut_commande
    
    def set_statut_commande(self, statut_commande):
        self.__statut_commande = statut_commande

    def set_liste_plats_commandes(self, liste_plats_commandes):
        self.__liste_plats_commandes = liste_plats_commandes

    def check_statut_commande(self):
        if self.__statut_commande == "En cours":
            print("La commande est en cours.")
        elif self.__statut_commande == "Terminée":
            print("La commande est terminée.")
        else:
            print("Le statut de la commande n'est pas valide.")

    def afficher_prix(self):
        for plat in self.__liste_plats_commandes:
            print(f"Le prix du plat {plat} est de {self.plat[plat]} euros.")

    def __calculer_prix_HT(self):
        prix = 0
        for plat in self.__liste_plats_commandes:
            prix += self.plat[plat]
        return f"Prix total HT : {prix} €"
    
    def __calculer_prix_TTC(self):
        prix = 0
        for plat in self.__liste_plats_commandes:
            prix += self.plat[plat]
        return (f"Prix total TTC : {round((prix * 1.2),2)} €")
        
    
commande1 = Commande(1, ["Pizza", "Pates"], "En cours")
commande2 = Commande(2, ["Frites", "Salade"], "Terminée")

commande1.get_numero_commande()
commande1.get_liste_plats_commandes()
commande1.set_statut_commande("En cours")
commande1.check_statut_commande()
commande1.set_annulation_commande()
commande1.get_liste_plats_commandes()
print(commande1._Commande__calculer_prix_HT())
print(commande1._Commande__calculer_prix_TTC())

commande2.get_numero_commande()
commande2.get_liste_plats_commandes()
commande2.ajout_plat("Pizza")
commande2.set_statut_commande("Terminée")
commande2.check_statut_commande()
commande2.afficher_prix()
print(commande2._Commande__calculer_prix_HT())
print(commande2._Commande__calculer_prix_TTC())