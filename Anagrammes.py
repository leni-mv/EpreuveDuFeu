#!/bin/python3.6

import sys

l1 = sys.argv[1]
f2 = sys.argv[2]

f1 = l1.splitlines()

with open(f2) as f:
    mots = f.read().splitlines()

#On vérifie que le mot que l'on recherche se trouve bien dans le fichier sélectionné et on place sont index dans une valeur "x":
if f1[0] in mots:
    x = mots.index(f1[0])

#Grâce à l'index du mot dans notre fichier on peut trouver les autres mots dont la longueur correspond:
anagram = ""
for i in mots:
    if len(i) == len(mots[x]):
        if i != mots[x]:
            x2 = mots.index(i)
            for j in mots[x2]:                        #Ensuite on compare la correspondance des lettres
                if sorted(mots[x2]) == sorted(f1[0]): 
                    anagram+=j                        
mot_trouvé = anagram.split()                   # On transforme le mot en liste.

#Et on additionne les deux listes !
f1+=mot_trouvé
print(f1)
            

