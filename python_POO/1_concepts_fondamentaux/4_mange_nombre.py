"""
Pour obtenir les nombres premiers compris entre 2 et un certain entier N on va construire une liste chaînéee d’objets
appelés des MangeNombres, chacun comportant deux variables d’instance :
- un nombre premier
- et une référence sur le MangeNombres suivant de la liste.
Le comportement d’un MangeNombres se réduit à l’opération ”manger un nombre”.

Le MangeNombres mp associé au nombre p mange les multiples de p :
si on lui donne à manger un nombre q qui n’est pas multiple de p,
mp le donne à manger à son MangeNombres suivant, s’il existe.
Si mp n’a pas de suivant, celui-ci est créé, associé à q.
La création d’un MangeNombres mp provoque l’affichage de p.

Définissez la classe MangeNombres et écrivez un programme affichant les nombres premiers entre 2 et N.

Liste Chaînée
Exemples
|2, ->None|
|2, ->3|--|3, ->None|
...
|2, ->3|--|3, ->5|--|5, ->7|--|7, ->None|


"""

