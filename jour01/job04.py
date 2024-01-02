class personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return "Bonjour, je m'appelle " + self.nom + " " + self.prenom + "."
    
Rija = personne("Rasoanaivo", "Rija")
Manon = personne("Rittling", "Manon")

print(Rija.SePresenter())
print(Manon.SePresenter())
