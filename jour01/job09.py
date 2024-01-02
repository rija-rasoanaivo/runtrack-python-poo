class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA    

    def CalculerPrixTTC(self):
        self.prixTTC = self.prixHT * (1 + self.TVA / 100)
        return f"Le prix TTC du {self.nom} est de : {round(self.prixTTC,2)} € TTC."    

    def CalculerTVA(self):
        coutTVA = self.prixHT * (self.TVA / 100)
        return f"Le taux de TVA du {self.nom} est de : {round(coutTVA,2)} %."    
    
    def modifierNom(self, nom):
        self.nom = nom
        return self.nom
    
    def modifierPrixHT(self, prixHT):
        self.prixHT = prixHT
        return self.prixHT
    
prixTTC = Produit("Pain", 1, 20)
print(prixTTC.nom)
print(prixTTC.CalculerTVA())
print(prixTTC.CalculerPrixTTC())

prixTTC.modifierNom("Pain au chocolat")
prixTTC.modifierPrixHT(5)
print(prixTTC.nom)
print(prixTTC.CalculerTVA())
print(prixTTC.CalculerPrixTTC())

prixTTC2 = Produit("Croissant", 15, 20)
print(prixTTC2.nom)
print(prixTTC2.CalculerTVA())
print(prixTTC2.CalculerPrixTTC())

prixTTC3 = Produit("Chausson aux pommes", 7, 20)
print(prixTTC3.nom)
print(prixTTC3.CalculerTVA())
print(prixTTC3.CalculerPrixTTC())

