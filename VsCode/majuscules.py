#!/bin/python3.6
#Une lettre sur deux en majuscule, les autres en minuscules !
#Yeah ! Tu PeUx Le FaIrE !!! \o/

a = input("Ecris ce que tu veux : ")
b = a.split()

i = b[0][0::2]
j = b[0][1::2]

for i, j in b:
    print(i.upper(), j.lower())