class ListePersonnes:
    def __init__(self):
        self.personnes = []

    def get_personnes(self):
        if len(self.personnes) > 0:
            return [[prs.get_nom(), prs.get_sexe(), prs.custom_get_adresses()] for prs in self.personnes]
        else:
            print("List is Empty")
            return False

    def set_personne(self, personne):
        self.personnes.append(personne)

    def find_by_nom(self, nom):
        peronnes = self.get_personnes()
        if peronnes:
            for personne in peronnes:
                if personne[0] == nom:
                    return personne
        return None

    def exit_code_postale(self, code):
        personnes = self.get_personnes()
        if personnes:
            for personne in personnes:
                adresses = personne[2]
                if len(adresses) > 0:
                    for adresse in adresses:
                        if adresse[2] == code:
                            return True
        return False

    def count_personne_ville(self, ville):
        count = 0
        personnes = self.get_personnes()
        if personnes:
            for personne in personnes:
                adresses = personne[2]
                if len(adresses) > 0:
                    for adresse in adresses:
                        if adresse[1] == ville:
                            count += 1
        return count

    def edit_personne_nom(self, oldNom, newNom):
        if len(self.personnes) > 0:
            for personne in self.personnes:
                if personne.get_nom() == oldNom:
                    personne.set_nom(newNom)

    def edit_personne_ville(self, oldVille, newVille):
        if len(self.personnes) > 0:
            for personne in self.personnes:
                adresses = personne.get_adresses()
                for adr in adresses:
                    if adr.get_ville() == oldVille:
                        adr.set_ville(newVille)
