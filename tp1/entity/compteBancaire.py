from sqlalchemy import column, Integer, Float, ForeignKey


class CompteBancaire:
    __tablename__ = 'comptebancaire'
    idCompte = column(Integer)
    solde = column(Float)
    decouver = column(Float)
    compte_id = column(Integer, ForeignKey('client.idClient'))

    def __init__(self, idCompte, solde, decouver):
        self.idCompte = idCompte
        self.solde = solde
        self.decouver = decouver

    def retrait(self, argent):
        if (self.solde < argent):
            print(" Impossible d'effectuer l'opération. Solde insuffisant !")
        else:
            self.solde = self.solde - argent
