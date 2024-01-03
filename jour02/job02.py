class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.titre = titre
        self.auteur = auteur
        self.nombre_de_pages = nombre_de_pages

    def get_titre(self):
        return self.titre
    
    def get_auteur(self):
        return self.auteur
    
    def get_nombre_de_pages(self):
        return self.nombre_de_pages
    
    def set_titre(self, titre):
        self.titre = titre

    def set_auteur(self, auteur):
        self.auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int):
            if nombre_de_pages >= 0:
                self.nombre_de_pages = nombre_de_pages
            else:
                self.nombre_de_pages = 0
                print("Le nombre de pages ne peut pas être négatif.")
        else:
            self.nombre_de_pages = 0
            print("Le nombre de pages doit être un entier.")

        
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1000)

print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nombre_de_pages())
livre1.set_titre("Harry Potter")
livre1.set_auteur("J.K. Rowling")
livre1.set_nombre_de_pages(10.5)
print(livre1.get_titre())
print(livre1.get_auteur())
print(livre1.get_nombre_de_pages())