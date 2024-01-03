class Student:
    def __init__(self, nom, prenom, numero_etudiants, nombre_de_credits):
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiants = numero_etudiants
        self.nombre_de_credits = nombre_de_credits 

    def set_add_credits(self, nombre_de_credits):
        if nombre_de_credits > 0:
            self.nombre_de_credits += nombre_de_credits
            print(f"Vous avez ajouté {nombre_de_credits} crédits.")
        else:
            print("Le nombre de crédits doit être positif.")

    def get_credits(self):
        print(f"Le nombre de credits de {self.prenom} {self.nom} est de {self.nombre_de_credits} crédits.")
        return self.nombre_de_credits


creditJohn = Student("Doe", "John", 12345, 0)
creditJohn.get_credits()
creditJohn.set_add_credits(5)
creditJohn.set_add_credits(5)
creditJohn.set_add_credits(-5)
creditJohn.set_add_credits(20)
creditJohn.get_credits()