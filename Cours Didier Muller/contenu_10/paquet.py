# Affichage de cartes mélangées

from random import randrange, shuffle
from tkinter import *
# from winsound import PlaySound


couleur = ('pique', 'trefle', 'carreau', 'coeur')
valeur = ('as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'valet', 'dame', 'roi')


class Carte(object):
    "Définition d'une carte"

    def __init__(self,val='as',coul='carreau'):
        self.valeur = val
        self.couleur = coul

    def dessin_carte(self):
        "Renvoi du nom du fichier image de la carte c"
        # les cartes sont dans le répertoire "cartes", au même niveau que ce programme
        nom = "cartes/"+self.valeur+"_"+self.couleur+".gif"
        return PhotoImage(file=nom)

        
class Paquet_de_cartes(object):
    """Paquet de cartes"""
    
    def __init__(self):
        "Construction de la liste des 52 cartes"
        self.cartes = []
        for coul in range(4):
            for val in range(13):
                nouvelle_carte = Carte(valeur[val], couleur[coul])   # la valeur commence à 1
                self.cartes.append(nouvelle_carte) 

    def battre(self):
        "Mélanger les cartes"
        # PlaySound("sons/distrib.wav",2)
        shuffle(self.cartes)

    def tirer(self):
        "Tirer la première carte de la pile"
        # PlaySound("sons/ramass.wav",1)
        t = len(self.cartes)
        if t>0:
            carte = self.cartes[0]   # choisir la première carte du jeu
            del(self.cartes[0])      # et la supprimer du jeu
            return carte
        else:
            return None


####################### Programme de test ##########################

def jouer():
    global carte1, lab1
    c = jeu.tirer()
    if c != None:
        carte1 = c.dessin_carte()
        lab1.configure(image=carte1)

def reinit():
    global jeu
    jeu = Paquet_de_cartes()
    jeu.battre()
    jouer()

# fenetre graphique

fenetre = Tk()
fenetre.title("Cartes")
jeu = Paquet_de_cartes()
jeu.battre()
c = jeu.tirer()
carte1 = c.dessin_carte()
lab1 = Label(fenetre, image=carte1)
lab1.grid(row=0, column=0)
bouton1 = Button(fenetre,text='Tirer',command=jouer)
bouton1.grid(row=1, column=0, sticky=W)
bouton4 = Button(fenetre,text='Recommencer',command=reinit)
bouton4.grid(row=2, column=0, sticky=E)

# demarrage :
fenetre.mainloop()  
