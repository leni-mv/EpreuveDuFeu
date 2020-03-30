#!/bin/python3.6

#fr.txt trouver les anagrammes

chemin = open("/home/leni/Pop/repos/EpreuveDuFeu/fr.txt")
mots = ""
for lignes in chemin:
    mots+=lignes
chemin.close
mots = mots.split()
b = []

#trier chaque lettres de chaque mots

#comparer chaque mot