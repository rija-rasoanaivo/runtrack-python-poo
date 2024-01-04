class CompteBancaire:
    def __init__(self, num_compte, nom, prenom, solde):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = True

    def get_num_compte(self):
        return self.__num_compte
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def set_num_compte(self, num_compte):
        self.__num_compte = num_compte

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_solde(self, solde):
        self.__solde = solde

    def afficher(self):
        print(f"Le compte n°{self.__num_compte} appartient a {self.__prenom} {self.__nom}.")

    def afficher_solde(self):
        print(f"Le solde du compte n°{self.__num_compte} est de {self.__solde} euros.")

    def versement(self, somme):
        self.__solde += somme
        print(f"Versement de {somme} euros sur le compte n°{self.__num_compte}.")
        
    def retrait(self, somme):
        if self.__decouvert == True:
            self.__solde -= somme
            print(f"Retrait de {somme} euros sur le compte n°{self.__num_compte}.")
        else:
            print(f"Retrait de {somme} euros impossible sur le compte n°{self.__num_compte}, vous n'avez assez d'argent sur votre compte.")

    def set_autorisations_decouvert(self, autorisations):
        self.__decouvert = autorisations

    def agios(self):
        if self.__solde < 0:
            self.__solde -= self.__solde * 0.03
            print(f"Agios de 3% appliques sur le compte n°{self.__num_compte}.")
        else:
            print(f"Agios non applicables sur le compte n°{self.__num_compte}.")

    def virement(self, somme, compte):
        self.__solde -= somme
        compte.__solde += somme
        print(f"Virement de {somme} euros du compte n°{self.__num_compte} vers le compte n°{compte.__num_compte}.")
        
compteRija = CompteBancaire(123, "Rasoanaivo", "Rija", 20000000)
compteYoucef = CompteBancaire(456, "Ouarlhent", "Youcef", -5000)

compteRija.afficher()
compteRija.afficher_solde()
compteRija.versement(1)
compteRija.afficher_solde()
compteRija.set_autorisations_decouvert(False)
compteRija.retrait(100000000000)
compteRija.retrait(10)
compteRija.afficher_solde()
compteRija.agios()
compteRija.afficher_solde()


compteYoucef.afficher()
compteYoucef.afficher_solde()
compteYoucef.set_autorisations_decouvert(True)
compteYoucef.agios()
compteRija.virement(5000, compteYoucef)
compteYoucef.afficher_solde()


