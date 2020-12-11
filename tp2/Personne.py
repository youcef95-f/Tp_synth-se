class Personne:
    def __init__(self, nome, sexe, adresse):
        self._nom = str(nome)
        self._sexe = str(sexe)
        self._adresses = [adresse]

    def get_nom(self):
        return self._nom

    def set_nom(self, nom):
        self._nom = str(nom)

    def get_sexe(self):
        return self._sexe

    def set_sexe(self, sexe):
        if sexe == "M" or sexe == "F":
            self._sexe = sexe
        else:
            print('Value Error , Valid Values : M or F')

    def custom_get_adresses(self):
        return [[i.get_rue(), i.get_ville(), i.get_code_postal()] for i in self._adresses]

    def set_adresse(self, adresse):
        self._adresses.append(adresse)

    def get_adresses(self):
        return self._adresses
