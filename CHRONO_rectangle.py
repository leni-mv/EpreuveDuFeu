#créer des index et liste de listes pour povoir noter la position
# quand position trouvée, vérifier que les chiffres suivant du tab 2 correspondent à ceux du tab 1
#14h23 - 16h25

p = open("/home/leni/Pop/repos/EpreuveDuFeu/file1.txt", "r")
G = open("/home/leni/Pop/repos/EpreuveDuFeu/file2.txt", "r")
#rendre la donnée manipulable
l1 = []
l2 = []
for lignes in p:
    l1 += lignes.split()
for lignes in G:
    l2 += lignes.split()

#comparer les deux tableau via fonction qu'on va mettre au dessus

def comparaison(l1, l2, x, i):
    x2 = 0
    y2 = 0
    while x2 < len(l1):
        if l1[x2][y2] == l2[x+x2][i+y2]:
            y2+=1
            if y2 == len(l1[x2]):
                x2+=1
                y2 = 0
        elif x2 == len(l1[0]) and y2 == len(l1):
            return True
        else:
            return False
    #l1 != l2
    #return False
    #elif return True
    #et on printera x et y"""


# comparer les chiffres premiers du l1 dans le l2
x = 0
y = 0
while x < len(l1):
    i = 0
    z = 0
    while i < len(l1[x]):       #"x" et "i" index de l2, "y" et "z" index de l1
        if l1[y][z] == l2[x + y][i + z]:
            comparaison(l1, l2, x, i)        #on a tout le tableau."""
            print(x, i)
        z+=1
        i+=1
    y+=1
    x+=1
