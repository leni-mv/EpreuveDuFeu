#!/bin/python3.6
#Crée un escalier à partir de n'importe quel nombre donné par l'utilisateur

n = input("Nombre de marche ici : ")
n = int(n)
b = "#"
a = 0

while a < n:
    print("{:>20s}".format(b))
    a = a + 1
    b = b + "#"
   
#Ce code est ma première idée : 
#il est fonctionnel mais comme on ne peut pas mettre un symbole "infinie" ou la variable "n" dans la fonction "format"
#(ligne 10), l'exercice ne peut pas être considéré comme réussie.
#Le nombre donné par l'utilisateur est limité par celui choisi dans la fonction "format".
