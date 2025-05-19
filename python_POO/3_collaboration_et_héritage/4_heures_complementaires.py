"""
Gestion d'heures complémentaires
Chaque enseignant de l’université effectue un certain nombre d’heures d’enseignement dans une année.
Suivant le statut de l’enseignant, un certain nombre de ces heures peut-être considéré comme complémentaire.

Les heures complémentaires sont payées séparément à l’enseignant.
Les volumes horaires sont exprimés en heures entières et le prix d’une heure complémentaire est de 10 Euros.
Le nom et le nombre d’heures total d’un enseignant sont fixés à sa création,
puis seul le nom peut être librement consulté (méthode nom()).
D’autre part on veut pouvoir librement consulter un enseignant sur son volume d’heures complémentaires (méthode hc())
 et sur la rétribution correspondante (méthode retribution()).
Il y a deux types d’enseignants :
    les intervenants extérieurs : toutes les heures effectuées sont complémentaires,
    les enseignants de la fac : seules les heures assurées au delà d’une charge statutaire de 192h sont complémentaires.

Comment modifier le modèle pour y introduire les  étudiants de troisième cycle qui assurent des enseignements :
 toutes les heures effectuées sont complémentaires mais dans la limite de 96 heures.
"""



gerard = Titulaire('Gerard', 195)
print(gerard.nom(), gerard.retribution())

germaine = Intervenant('Germaine', 520)
print(germaine.nom(), germaine.retribution())

gaston = Etudiant('Gaston', 12)
print(gaston.nom(), gaston.retribution())

