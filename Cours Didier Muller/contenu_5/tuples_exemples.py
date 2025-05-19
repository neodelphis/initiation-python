# tuples

mon_tuple = ('a', 4, "coucou", ('autre', 'tuple'))

for element in mon_tuple:
    print(element)

print('mon_tuple[2] : ', mon_tuple[2])

# mon_tuple[2] = 3  # Erreur
exemple = 1, 2
print(exemple)

# unpack
a, b = exemple
print('a : ', a)
print('b : ', b)

for i, element in enumerate(mon_tuple):
    print('mon_tuple[', i, '] =  ', element)

liste_ex = list(exemple)
liste_ex[1] = 3
print(liste_ex)

exemple = tuple(liste_ex)
print(exemple)
