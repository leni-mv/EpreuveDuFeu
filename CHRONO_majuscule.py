#!/bin/python3.6
#14h41 #15h16 je recommence tout à cause des " " que j'arrive pas à gérer dans une liste TwT
#15h32 #51min en regardand ce que j'ai fais pour la gestion des " "

string = input("Ecris ce que tu veux :")
longueur = 0
clean = ""

for i in string:
    if i == " ":
        len(string) == " " * 2
        clean += i
        longueur+=1
    if longueur % 2 == 0:
        clean += i.upper()
        longueur+=1
    elif longueur % 2 == 1:
        clean += i.lower()
        longueur+=1

print(clean)
