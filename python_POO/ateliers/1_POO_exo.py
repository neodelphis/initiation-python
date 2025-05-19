# Exercice d'application
# # Entreprise de téléphones
# # Numéro de série en sortie d'usine
# # Mise en route: attribution d'un numéro de tel, si opérateur SFR, Orange, Free
# Créer 3 téléphones, afficher leur numéro de série
# Essayer de mettre un numéro de tél au premier chez SFR: 01 02 03
# Essayer de mettre un numéro de tél au second chez TOTOCOM: 01 01 01


class Telephone:
    def __init__(self, numero_de_serie=0):
        self.numero_de_serie = numero_de_serie
        self.numero_de_telephone = None

    def attribuer_un_numero(self, numero_de_telephone, operateur):
        if operateur in ['SFR', 'Orange', 'Free']:
            self.numero_de_telephone = numero_de_telephone


tel_1 = Telephone(498412)
tel_2 = Telephone()
tel_3 = Telephone('Neuf')

# print('*** numero_de_serie ***')
# print(tel_1.numero_de_serie)
# print(tel_2.numero_de_serie)
# print(tel_3.numero_de_serie)

tel_1.attribuer_un_numero('01 02 03', 'SFR')
tel_2.attribuer_un_numero('01 01 01', 'TOTOCOM')

# print('*** numero_de_telephone ***')
print(tel_1.numero_de_telephone)
print(tel_2.numero_de_telephone)
