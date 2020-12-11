from Adresse import *
from ListePersonnes import *
from Personne import *

adr = Adresse("Rue X", "Paris", "0000")
adr1 = Adresse("Rue Z", "Nice", "1111")
adr2 = Adresse("Rue E", "Nice", "1001")
adr3 = Adresse("Rue M", "Paris", "1122")

prs = Personne("Forar", "M", adr)
prs.set_adresse(adr1)
prs1 = Personne("Youcef", "M", adr2)
prs2 = Personne("Mick", "M", adr3)

ListePersonnes = ListePersonnes()
ListePersonnes.set_personne(prs)
ListePersonnes.set_personne(prs1)
ListePersonnes.set_personne(prs2)

personnes = ListePersonnes.get_personnes()
print(personnes)
exist_code = ListePersonnes.exit_code_postale("000")
personnes_per_ville = ListePersonnes.count_personne_ville("Paris")

ListePersonnes.edit_personne_nom("Mick", "Jhon")
ListePersonnes.edit_personne_ville("Nice", "Monaco")

personnes = ListePersonnes.get_personnes()

print(personnes)
