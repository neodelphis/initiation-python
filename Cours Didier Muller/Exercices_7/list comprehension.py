# List comprehension
# Contruction compacte de listes

nombres = [1, 2, 3]

# Liste des carrés
carres = []
for nombre in nombres:
    carres.append(nombre * nombre)
print(carres)

# Définition compacte
carres = [nombre ** 2 for nombre in nombres]

# Définition compacte avec condition
carres = [nombre ** 2 for nombre in nombres if nombre > 1]
print(carres)
