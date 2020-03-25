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
f2.close()#!/bin/python3.6

f1 = open("/home/leni/Pop/repos/EpreuveDuFeu/file1.txt", "r")
f2 = open("/home/leni/Pop/repos/EpreuveDuFeu/file2.txt", "r")
l1 = []
l2 = []

for ligne in f1: #mise des valeurs du fichier1 dans une
    l1+=ligne    #variable manipulable !
f1.close()
print(l1)

for ligne in f2: #mise des valeurs du fichier2 dans une
    l2+=ligne    #variable manipulable !
f2.close()
print(l2)

b = ""
for i in l1:
    b+=i

print(b)