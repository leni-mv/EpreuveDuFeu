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
def liste_temoin():
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = []
    for i in b:
        i = str(i)
        n+=i
    return n

while l < len(s2):
    l = 0
    while c < len(s2[l]):   #ça ça fonctionne !
        c = 0
        n = liste_temoin()
        x = 0
        if c in n[x]:      #ça ça fonctionne pas
            print("ok")
  #          if c == n[x]:   #pour garder dans n ce qui n'est pas dans len(l)...
   #             n.pop(x)
    #            c+=1
     #       elif c != n[x]: #...pour que le reste de n comble trous de l
      #         x+=1
       #     elif s2[l][c] == "_":
        #        s2[l][c].replace("_", n[x])
         #       x+=1
          #  c+=1
        else:
            c+=1
  #  l+=1
#print(s2)



#Créer 3 fonctions secondaires pour vérifier lignes, colonnes, carrés
#Créer fonction lignes
test = "1230456789"
for i in test:
    if i == "0":
        while "0" in test:
            n = "123456789"
            for n - test:
                test.replace(i, n)
        print(test)