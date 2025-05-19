# jeu pierre, papier, ciseaux
# l'ordinateur joue au hasard

from random import randint

def ecrire(nombre):
    if nombre == 1:
        print("pierre",end=" ")
    elif nombre ==2:
        print("papier",end=" ")
    else :
        print("ciseaux",end=" ")

def augmenter_scores(mon_coup,ton_coup,mon_score,ton_score):
    mon_nouveau_score = mon_score
    ton_nouveau_score = ton_score
    if mon_coup == 1 and ton_coup == 2:
        ton_nouveau_score += 1
    elif mon_coup == 2 and ton_coup == 1:
        mon_nouveau_score += 1
    elif mon_coup == 1 and ton_coup == 3:
        mon_nouveau_score += 1
    elif mon_coup == 3 and ton_coup == 1:
        ton_nouveau_score += 1
    elif mon_coup == 3 and ton_coup == 2:
        mon_nouveau_score += 1
    elif mon_coup == 2 and ton_coup == 3:
        ton_nouveau_score += 1
    return mon_nouveau_score, ton_nouveau_score
        
ton_score = 0
mon_score = 0
fin = 5
print("Pierre-papier-ciseaux. Le premier à",fin,"a gagné !")
no_manche = 0
while mon_score < fin and ton_score < fin:
    ton_coup = int(input("1 : pierre, 2 : papier, 3 : ciseaux ? "))
    while ton_coup < 1 or ton_coup > 3:
        ton_coup =int(input("1 : pierre, 2 : papier, 3 : ciseaux ? "))
    print("Vous montrez",end=" ")
    ecrire(ton_coup)
    mon_coup = randint(1,3)
    print("- Je montre",end=" ")
    ecrire(mon_coup)
    print()     # aller à la ligne
    mon_score,ton_score=augmenter_scores(mon_coup,ton_coup,mon_score,ton_score)
    print("vous",ton_score,"   moi",mon_score)

                  
