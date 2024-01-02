class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon
        return self.rayon
    
    def afficherInfos(self):
        print(self.circonference())
        print(self.aire())
        print(f"Le rayon est de : {self.rayon} cm")
        print(self.diametre())

    def circonference(self):
        return "La circonférence du cercle est de " + str(2 * 3.14 * self.rayon) + " cm."
    
    def aire(self):
        return "L'aire du cercle est de " + str(3.14 * self.rayon ** 2) + " cm²."
    

    def diametre(self):
        return "Le diamètre du cercle est de " + str(2 * self.rayon) + " cm."
    
Cercle1 = Cercle(4)
Cercle1.afficherInfos()
Cercle1.changerRayon(9)
Cercle1.afficherInfos()

Cercle2 = Cercle(7)
Cercle2.afficherInfos()
Cercle2.changerRayon(12)
Cercle2.afficherInfos()