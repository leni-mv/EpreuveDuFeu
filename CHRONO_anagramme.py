#!/bin/python3.6
# Anagramme refait en moins de 3h (8h17-10h52)
import sys

file = open("/home/leni/Pop/repos/EpreuveDuFeu/fr.txt", "r")  #associer fichier à utiliser
mot = sys.argv[1]

l1 = ""
for ligne in file: #mise des valeurs du fichier1 dans une variable manipulable !
    l1+=ligne    
file.close()
#passage de liste à array pour l1:
l1 = l1.split()

#comparer len des mots

l2 = []
for i in l1:
    x = 1
    while x < len(l1):
        if len(i) == len(l1[x]):
            l2 += i.split()
        else:
            x+=1
        x+=1

#transformer mots en listes pour pouvoir trier lettres
#x = 0
while x < len(l2):
    l2[x] = list(l2[x])
    x+=1

mot = list(mot)

#comparer lettres triée à mot trié
i = 0
resultat = []
while i < len(l2):
    if sorted(l2[i]) == sorted(mot):
        print(l2[i])
    i+=1

