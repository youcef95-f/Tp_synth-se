class Adresse:
    def __init__(self, rue, ville, code_postal):
        self._rue = str(rue)
        self._ville = str(ville)
        self._code_postal = str(code_postal)

    def get_rue(self):
        return self._rue

    def set_rue(self, rue):
        self._rue = str(rue)

    def get_ville(self):
        return self._ville

    def set_ville(self, ville):
        self._ville = str(ville)

    def get_code_postal(self):
        return self._code_postal

    def set_code_postal(self, code_postal):
        self._code_postal = str(code_postal)
