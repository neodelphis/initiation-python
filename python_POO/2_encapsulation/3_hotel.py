"""
https://www.freecodecamp.org/news/python-property-decorator/

On souhaite écrire une classe `Hotel`. Pour cet exercice, un hôtel sera caractérisé par :
– son nom : une chaîne de caractères
– son nombre de chambres : un entier strictement positif

Le nombre de chambres est toujours connu dès la création d’un objet de type Hotel.
Il doit être possible de créer un objet Hotel en précisant son nom ou sans le préciser.
Le nom de l’hôtel doit pourvoir être modifié.
Une tentative de modification du nombre de chambre doit générer un erreur.

Enfin, sur tous les objets Hotel, il faut pouvoir :
– accéder aux valeurs de chacun des attributs ;
– modifier les attributs qui doivent pouvoir être modifiés ;
– récupérer une représentation textuelle de l’état de l’hôtel (méthode __str__())

Ecrire la classe correspondante et un ensemble de test détaillant les différentes configurations possibles
"""
