class Animal:
    def __init__(self, age, prenom):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        return self.age
    
    def nommer(self, prenom):
        self.prenom = prenom
        return self.prenom

Animal = Animal(0, "")
print("L'age de l'animal",Animal.age ,"ans")
Animal.vieillir()
print("L'age de l'animal",Animal.age ,"ans")
Animal.nommer("Luna")
print("L'animal de nomme",Animal.prenom)