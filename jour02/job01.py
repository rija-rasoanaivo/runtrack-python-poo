class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def get_longueur(self):
        return self.longueur
    
    def get_largeur(self):
        return self.largeur
    
    def set_longueur(self, longueur):
        self.longueur = longueur

    def set_largeur(self, largeur):
        self.largeur = largeur

rectangle1 = Rectangle(10, 5)

print(rectangle1.get_longueur())
print(rectangle1.get_largeur())
rectangle1.set_longueur(60)
rectangle1.set_largeur(30)
print(rectangle1.get_longueur())
print(rectangle1.get_largeur())