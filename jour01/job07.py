class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
        return self.x
    
    def droite(self):
        self.x += 1
        return self.x
    
    def bas(self):
        self.y -= 1
        return self.y
    
    def haut(self):
        self.y += 1
        return self.y
    
    def position(self):
        return "x = " + str(self.x) , " y = " + str(self.y)
    
position_personnage = Personnage(0, 0)
print(position_personnage.position())
position_personnage.gauche()
print(position_personnage.position())
position_personnage.droite()
print(position_personnage.position())
position_personnage.bas()
print(position_personnage.position())
position_personnage.haut()
print(position_personnage.position())