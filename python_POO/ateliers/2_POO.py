class Maison:
    def __init__(self, nombre_de_pieces=1):
        self.nombre_de_pieces = nombre_de_pieces
        self.couleur = None

    def peindre(self, c):
        if c in ['bleu', 'blanc']:
            self.couleur = c

    # def affiche(self):
    #     print("Ma maison " + str(self.nombre_de_pieces) + " pièces, de couleur " + str(self.couleur))

    def __repr__(self):
        return f'{str(self.nombre_de_pieces)} pièces, de couleur {str(self.couleur)}'


maison_1 = Maison(3)
# maison_2 = Maison(4)

maison_1.peindre('bleu')
# maison_2.peindre('rouge')

# maison_1.affiche()
print(maison_1)
# print(maison_2)

# print(maison_1.nombre_de_pieces)
# print(maison_1.couleur)

# print(maison_2.nombre_de_pieces)
# print(maison_2.couleur)

# print(maison_1)
