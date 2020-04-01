import sys

s1 = "/home/leni/Pop/repos/EpreuveDuFeu/s.txt"

with open(s1) as f:
    s2 = f.read().splitlines()
print(s2)
# variables d'index, l=lignes, c=colonnes, c4= carrés
l = 0
c = 0
c4 = [0, 1, 2]
"""Soit on définie une/des valeurs spécifiques pour les
carrés, Soit on délimite l et c : s2[l:l+2][c:c+2]




