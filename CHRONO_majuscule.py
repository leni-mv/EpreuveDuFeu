#!/bin/python3.6
#Entre 14h41 et 15h32

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
