class operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def getNombre(self):
        print("Le nombre 1 est :", self.nombre1) 
        print("Le nombre 2 est :", self.nombre2)

valeur_attribut = operation(10, 12)
valeur_attribut.getNombre()