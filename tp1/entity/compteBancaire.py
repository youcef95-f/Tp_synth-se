class CompteBancaire:
    def __init__(self, idCompte, solde, decouver):
        self.idCompte = idCompte
        self.solde = solde
        self.decouver = decouver

    def retrait(self, argent):
        if (self.solde < argent):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent

    def retirer(self, idCcoompte, montant):

