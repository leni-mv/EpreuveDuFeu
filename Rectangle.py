#!/bin/python3.6

f1 = open("/home/leni/Pop/repos/EpreuveDuFeu/file1.txt", "r")
f2 = open("/home/leni/Pop/repos/EpreuveDuFeu/file2.txt", "r")
l1 = ""
l2 = ""

for ligne in f1: #mise des valeurs du fichier1 dans une
    l1+=ligne    #variable manipulable !
f1.close()
#passage de liste à array pour l1:
l1 = l1.split()

for ligne in f2: #mise des valeurs du fichier2 dans une
    l2+=ligne    #variable manipulable !
f2.close()
#passage de liste à array pour l2:
l2 = l2.split()

def suite(l1, l2, x, y):
    x2 = 0
    while x2 < len(l1):
        y2 = 0
        while y2 < len(l1):
            if l1[x2][y2] != l2[x + x2][y + y2]:
                return False
            else:
                y2+=1
        x2+=1
    return True

def rectangle(l1, l2):
    x = 0
    x2 = 0
    while x < len(l2):
        y = 0
        y2 = 0
        while y < len(l2[x]):
            if l2[x][y] == l1[0][0]:
                suite(l1, l2, x, y)
                print(f"{x}, {y}")
                return True
            elif l2[x][y] != l1[0][0]:
                y+=1
        x+=1
    print("pas trouvé ~-~")
    return False
            
rectangle(l1, l2)