class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__prix = prix

    def get__marque(self):
        return self.__marque
    
    def get__modele(self):
        return self.__modele
    
    def get__annee(self):
        return self.__annee
    
    def get__prix(self):
        return self.__prix
    
    def set__marque(self, marque):
        self.__marque = marque

    def set__modele(self, modele):
        self.__modele = modele

    def set__annee(self, annee):
        self.__annee = annee

    def set__prix(self, prix):
        self.__prix = prix

    def informationsVehicule(self):
        return "Marque: " + self.__marque + "\nModèle: " + self.__modele + "\nAnnée: " + str(self.__annee) + "\nPrix: " + str(self.__prix) + " €"
    
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, nbPortes = 4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.__nbPortes = nbPortes
    
    def get__nbPortes(self):
        return self.__nbPortes 
    
    def set__nbPortes(self, nbPortes):
        self.__nbPortes = nbPortes

    def informationsVehicule(self):
        return "Marque: " + self.get__marque() + "\nModèle: " + self.get__modele() + "\nAnnée: " + str(self.get__annee()) + "\nPrix: " + str(self.get__prix()) + " €" + "\nNombre de portes: " + str(self.__nbPortes)
    
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roues=2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.__roues = roues

    def get__roues(self):
        return self.__roues
    
    def set__roues(self, roues):
        self.__roues = roues

    def informationsVehicule(self):
        return "Marque: " + self.get__marque() + "\nModèle: " + self.get__modele() + "\nAnnée: " + str(self.get__annee()) + "\nPrix: " + str(self.get__prix()) + " €" + "\nNombre de roues: " + str(self.get__roues())

Clio = Voiture("Renault", "Clio", 2019, 15000)
print(Clio.informationsVehicule())
print(Clio.get__nbPortes())
Clio.set__nbPortes(5)
print(Clio.get__nbPortes())
print(Clio.informationsVehicule())

Moto1 = Moto("Yamaha", "MT-07", 2019, 7000)
print(Moto1.informationsVehicule())

