import sys

s1 = "/home/leni/Pop/repos/EpreuveDuFeu/s.txt"
s2 = ""
with open(s1) as f:
    s2 = f.read().splitlines()
print(s2)
print(s2[4])
#assainir les listes de la liste des caractères inutiles.
#sélectionner caractères spéciaux dans les listes
for i in s2:
    s2.remove("|")

print(s2)




#Créer 3 fonctions secondaires pour vérifier lignes, colonnes, carrés
#Créer une fonction principale pour vérifier les 3 secondaire
#rajouté les caractères spéciaux et print la liste