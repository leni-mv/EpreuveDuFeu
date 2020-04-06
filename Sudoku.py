#!/bin/python3.6

import sys

s1 = "/home/leni/Pop/repos/EpreuveDuFeu/s.txt"
s2 = ""
with open(s1) as f:
    s2 = f.read().splitlines()
x = 0
for i in s2[x]:
    if i == "|":
        print("yes sir")
        x+=1
    else:
        x+=1
    x+=1



#assainir les listes de la liste des caractères inutiles.
#sélectionner caractères spéciaux dans les listes





#Créer 3 fonctions secondaires pour vérifier lignes, colonnes, carrés
#Créer une fonction principale pour vérifier les 3 secondaire
#rajouté les caractères spéciaux et print la liste