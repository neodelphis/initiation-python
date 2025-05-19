# Le jeu possède 4 règles :

# 1. Le Joueur 1 choisit un nombre entre 1 et Nmax
# 2. A tour de rôle, chaque joueur doit choisir un nombre parmi les multiples
#    ou les diviseurs du nombre choisi précédemment par son adversaire
#    et inférieur à Nmax.
# 3. Un nombre ne peut être joué qu'une seule fois.
# 4. Le premier nombre choisi doit être pair.

# Le perdant est le joueur qui ne trouve plus de multiples ou de diviseurs
# communs au nombre précédemment choisi.

from random import randint

def multiples(n):
    #renvoie la liste des multiples de n <= Nmax
    mult=[]
    i=2
    while i*n <= Nmax :
        if i*n in possibles:    # on l'ajoute seulement s'il n'a pas été joué
            mult.append(i*n)
        i += 1
    return mult

def diviseurs(n):
    #renvoie la liste des diviseurs de n
    div = []
    i=n
    while i >= 1:
        if n%i == 0 and n//i in possibles:    # on l'ajoute s'il n'a pas été joué
            div.append(n//i)
        i-=1
    return div


Nmax = 20
possibles = list(range(1,Nmax+1))   # liste des nombres pas encore utilisés
mon_nombre=2*randint(1,Nmax/2)      # l'ordinateur choisit un nombre pair
possibles.remove(mon_nombre)        # on enlèvera de la liste "possibles" tous les nombres joués

# Début du jeu

print("Jouons avec des nombres entre 1 et",Nmax)
print("Je choisis comme nombre de départ",mon_nombre)
valides = diviseurs(mon_nombre) + multiples(mon_nombre)
while valides != []:
    print("Nombres valides :",valides)
    ton_nombre=int(input("Que jouez-vous ? "))
    while ton_nombre not in valides:
        ton_nombre=int(input("Incorrect. Que jouez-vous ? "))
    possibles.remove(ton_nombre)
    valides = diviseurs(ton_nombre) + multiples(ton_nombre)
    if valides == []:
        print("Bravo!")
    else:
        mon_nombre = valides[randint(0,len(valides)-1)]
        print("Nombres valides :",valides)
        print("Je joue",mon_nombre)
        possibles.remove(mon_nombre)        
        valides = diviseurs(mon_nombre) + multiples(mon_nombre)
        if valides == []:
            print("Vous avez perdu!")
