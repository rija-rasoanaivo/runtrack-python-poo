class Student:
    def __init__(self, nom, prenom, numero_etudiants, nombre_de_credits):
        self.nom = nom
        self.prenom = prenom
        self.numero_etudiants = numero_etudiants
        self.nombre_de_credits = nombre_de_credits 

    def get_ID(self):
        print(f"Le nom de l'étudiant est {self.prenom} {self.nom}, sont ID est :{self.numero_etudiants}.")
        return self.nom, self.prenom, self.numero_etudiants
    
    def get_prenom(self):
        return self.prenom
    
    def get_numero_etudiants(self):
        return self.numero_etudiants

    def set_add_credits(self, nombre_de_credits):
        if nombre_de_credits > 0:
            self.nombre_de_credits += nombre_de_credits
            print(f"Vous avez ajouté {nombre_de_credits} crédits.")
        else:
            print("Le nombre de crédits doit être positif.")

    def get_credits(self):
        print(f"Le nombre de credits de {self.prenom} {self.nom} est de {self.nombre_de_credits} crédits.")
        return self.nombre_de_credits


creditJohn = Student("Doe", "John", 145, 0)
creditJohn.get_ID()
creditJohn.get_credits()
creditJohn.set_add_credits(5)
creditJohn.set_add_credits(5)
creditJohn.set_add_credits(-5)
creditJohn.set_add_credits(20)
creditJohn.get_credits()