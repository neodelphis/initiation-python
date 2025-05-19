class Maison:
    def __init__(self, nombre_de_pieces = 1):
        self.nombre_de_pieces = nombre_de_pieces
        self.couleur = None

    def peindre(self, c):
        if c in ['bleu', 'rouge']:
            self.couleur = c


maison_1 = Maison()
maison_2 = Maison(4)

# print(maison_1)
maison_1.peindre('bleu')
# maison_2.peindre('rouge')

# print(maison_1.couleur)
# print(maison_2.nombre_de_pieces)
print(maison_1)
