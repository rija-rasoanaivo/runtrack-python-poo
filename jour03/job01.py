class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom_ville = nom
        self.__nb_habitants = nb_habitants

    def get_nom_ville(self):
        return self.__nom_ville
    
    def get_nb_habitants(self):
        print(f"Population de la ville de {self.__nom_ville} : {self.__nb_habitants} habitants.")
        return self.__nb_habitants
    
    def set_nom_ville(self, nom):
        self.__nom_ville = nom

    def set_nb_habitants(self, nb_habitants):
        self.__nb_habitants = nb_habitants

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom_personne = nom
        self.__age = age
        self.__ville = ville

    def get_nom_personne(self):
        return self.__nom_personne
    
    def get_age(self):
        return self.__age
    
    def get_ville(self):
        return self.__ville
    
    def set_nom_personne(self, nom):
        self.__nom_personne = nom

    def set_age(self, age):
        self.__age = age

    def set_ville(self, ville):
        self.__ville = ville

    def ajouterPopulation(self):
        self.__nb_habitants = self.__ville.get_nb_habitants() + 1
        self.__ville.set_nb_habitants(self.__nb_habitants)
        print(f"Mise a jour de la population de la ville de {self.__ville.get_nom_ville()} {self.__ville.get_nb_habitants()} habitants.")
        

Paris = Ville("Paris", 1000000)
print(Paris.get_nb_habitants())

Marseille = Ville("Marseille", 861635)
print(Marseille.get_nb_habitants())

John = Personne("John", 45, Paris)
John.ajouterPopulation()

Myrtille = Personne("Myrtille", 4, Paris)
Myrtille.ajouterPopulation()

Chloe = Personne("Chloé", 18, Marseille)
Chloe.ajouterPopulation()