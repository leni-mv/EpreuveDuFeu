#!/bin/python3.6

f1 = open("/home/leni/Pop/repos/EpreuveDuFeu/file1.txt", "r")
f2 = open("/home/leni/Pop/repos/EpreuveDuFeu/file2.txt", "r")
l1 = ""
l2 = ""

for ligne in f1: #mise des valeurs du fichier1 dans une
    l1+=ligne    #variable manipulable !
f1.close()
print(l1)


for ligne in f2: #mise des valeurs du fichier2 dans une
    l2+=ligne    #variable manipulable !
f2.close()
print(l2)

#création d'une fonction pour "colorier"
#valeurs de l2 identiques à l1.
"""
def dépistage():
    for i in l2:
        if i == l1:
            colorier i
            print(i)
        elif i != l1:
            print(i)
        else:
            print("La fonction fonctionne !")
"""



for l1 in l2:           #Boucle qui vérifie présence des
    if l1 in l2:        #valeur de l1 dans l2
        for i in l2:
            if i == l1:
                #colorier i
                print(i)
            elif i != l1:
                print(i)
            else:
                print("La fonction fonctionne !")
    else:
        print("la boucle fonctionne")
        break


