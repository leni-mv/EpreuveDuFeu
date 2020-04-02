import sys

s1 = "/home/leni/Pop/repos/EpreuveDuFeu/s.txt"
s2 = ""
with open(s1) as f:
    s2 = f.read().splitlines()

# variables d'index, l=lignes, c=colonnes, c4= carrés
l = 0
c = 0
c4 = [0, 1, 2]

#création de la variable qui va vérifier chaque valeurs
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = []
for i in n:
    i = str(i)
    n+=i

while l < len(s2): #ça ça fonctionne !
    l = 0
    while c < len(s2[l]):
        x = 0
        if c == "|":
            c+=1
        elif c == "-":
            l+=1
        elif s2[l][c] in n[x]:      #Erreur index or de la liste
            print("n")
            #if s2[l][c] == n:
             #   n-=s2[l][c]
              #   c+=1
            #elif s2[l][c] == "_":
             #   s2[l][c]+=n
        c+=1
    l+=1
print(s2)