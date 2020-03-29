#!/bin/python3.6

#fr.txt trouver les anagrammes

chemin = open("/home/leni/Pop/repos/EpreuveDuFeu/fr.txt")
mots = ""
for lignes in chemin:
    mots+=lignes
chemin.close
mots = mots.split()

mot2 = 0
l1 = 0
l2 = 0
n = 0

for mot1 in mots:
    print(mot1)
    print()
    for mot2 in mots:
        print(mot2)
    
    

