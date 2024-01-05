class Personne:
    def __init__(self, age = int(14)):
        self.age = age

    def afficherAge(self):
        print("Age : ", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

class Professeur(Personne):
    def __init__(self):
        self.__matiereEnseignee = "Mathematiques"

    def get__matiereEnseignee(self):
        return self.__matiereEnseignee
    
    def set__MatiereEnseignee(self, matiere):
        self.__matiereEnseignee = matiere

    def enseigner(self):
        print("Le cours va commencer")


Etudiant = Eleve()
Etudiant.afficherAge()
Etudiant.bonjour()
Etudiant.allerEnCours()
Etudiant.afficherAge()
Etudiant.modifierAge(15)
Etudiant.afficherAge()

Prof = Professeur()
Prof.modifierAge(40)
Prof.afficherAge()
print(Prof.get__matiereEnseignee())
Prof.enseigner()

personne = Personne()
personne.afficherAge()
personne.bonjour()