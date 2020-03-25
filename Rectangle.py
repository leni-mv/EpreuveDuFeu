#!/bin/python3.6

f1 = open("/home/leni/Pop/repos/EpreuveDuFeu/file1.txt", "r")
f2 = open("/home/leni/Pop/repos/EpreuveDuFeu/file2.txt", "r")
l1 = ""
l2 = ""

for ligne in f1: #mise des valeurs du fichier1 dans une
    l1+=ligne    #variable manipulable !
f1.close()


for ligne in f2: #mise des valeurs du fichier2 dans une
    l2+=ligne    #variable manipulable !
f2.close()

print(l1)
print(l2)
print(len(l2))
print()

b = ""
j = 0

for i in l2:        #boucle pour "colorier"
    if i == l1.isdigit():     #valeurs de l2 identiques à l1.
        b = '\033[35m' + i + '\033[0m'
        j+=1     
    elif i != l1:
        b+=i
        j+=1
    else:
        j == len(l2)
        break

print(b)