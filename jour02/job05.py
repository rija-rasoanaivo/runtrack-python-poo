class Voiture:
    def __init__(self, marque, modele, annee, kilometrage, en_marche = False):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.kilometrage = kilometrage
        self.en_marche = en_marche
        self.reservoir = 50

    def get_marque(self):
        return self.marque
    
    def get_modele(self):
        return self.modele
    
    def get_annee(self):
        return self.annee
    
    def get_kilometrage(self):
        return self.kilometrage
    
    def get_en_marche(self):
        return self.en_marche
    
    def set_marque(self, marque):
        self.marque = marque

    def set_modele(self, modele):
        self.modele = modele

    def set_annee(self, annee):
        self.annee = annee

    def set_kilometrage(self, kilometrage):
        self.kilometrage = kilometrage

    def set_en_marche(self, en_marche):
        self.en_marche = en_marche

    def demarrer(self):
        if self.en_marche == False:
            if self.__verifier_plein() > 5:
                self.en_marche = True
                print("La voiture démarre.")
            else:
                print("Le réservoir est vide.")
        else:
            print("La voiture est déjà en marche.")

    def arreter(self):
        if self.en_marche == True:
            self.en_marche = False
            print("La voiture est arrêtée.")
        else:
            print("La voiture est déjà arrêtée.")

    def __verifier_plein(self):
        return self.reservoir
    
    def set_reservoir(self, reservoir):
        self.reservoir = reservoir

BMW = Voiture("BMW", "Serie 3", 2019, 126300, False)

print(BMW.get_marque())
print(BMW.get_modele())
print(BMW.get_annee())
print(BMW.get_kilometrage())
print(BMW.get_en_marche())
BMW.demarrer()
print(BMW.get_en_marche())
BMW.arreter()
print(BMW.get_en_marche())
BMW.set_reservoir(2)
BMW.demarrer()

