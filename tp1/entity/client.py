from sqlalchemy import column, String, Integer


class Client:
    __tablename__ = 'client'
    idClient = column(Integer)
    Civilite = column(String)
    nom = column(String)
    prenom = column(String)
    adresse = column(String)
    adresse = column(String)

    def __init__(self, idClient, Civilite, nom, prenom, adresse):
        self.idClient = idClient
        self.Civilite = Civilite
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
