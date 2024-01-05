class Forme:
    def aire(self):
        return 0

    def get_aire(self):
        return self.__aire
    
    def set_aire(self, aire):
        self.__aire = aire


class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.__largeur = largeur
        self.__hauteur = hauteur

    def get__largeur(self):
        return self.__largeur
    
    def get__hauteur(self):
        return self.__hauteur
    
    def set__largeur(self, largeur):
        self.__largeur = largeur

    def set__hauteur(self, hauteur):
        self.__hauteur = hauteur

    def aire(self):
        self.set_aire(self.__largeur * self.__hauteur)
        return self.get_aire()
    
forme = Forme()
print(forme.aire())

rectangle = Rectangle(5, 4)
print(rectangle.aire())


