class CompteBancaire:

    def __init__(self, idCompte, solde, decouvert):
        self.idCompte = idCompte
        self.solde = solde
        self.decouvert = decouvert

    def retrait(self, montant):
        facilitesCaisse = self.decouvert
        if self.solde + facilitesCaisse < montant:
           raise Exception('Slode insuffisant')
        else:
            self.solde = self.solde - montant

    def ajouter(self, montant):
        self.solde += montant