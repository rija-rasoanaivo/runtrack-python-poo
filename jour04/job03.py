class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get__longueur(self):
        return self.__longueur
    
    def get__largeur(self):
        return self.__largeur
    
    def set__longueur(self, longueur):
        self.__longueur = longueur

    def set__largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur
    
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def get__hauteur(self):
        return self.__hauteur
    
    
    def set__hauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return  self.__hauteur * Rectangle.surface(self)
    
    def afficherVolume(self):
        print(f"Le volume est de {self.volume()}")
    



Rectangle1 = Rectangle(5, 4)

print(Rectangle1.perimetre())
print(Rectangle1.surface())

Rectangle1.get__longueur()
Rectangle1.get__largeur()
Rectangle1.set__longueur(10)
Rectangle1.set__largeur(8)
print(Rectangle1.perimetre())
print(Rectangle1.surface())

Parallelepipede1 = Parallelepipede(5, 4, 3)
Parallelepipede1.afficherVolume()



