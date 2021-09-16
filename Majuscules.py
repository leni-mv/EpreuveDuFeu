#!/bin/python3.6
#Une lettre sur deux en majuscule, les autres en minuscules !

a = input("Ecris les mots ou les phrases que tu veux : ")
j = 0
b = ""

for i in a:
    if i == " ":
        len(a) == " " * 2
        b += i
        j != j
    elif j % 2 == 1:
        b += i.lower()
        j+=1
    elif j % 2 == 0:
        b += i.upper()
        j+=1
    elif j == len(a):
        break

print(b)
