#!/bin/python3.6

import sys

s1 = "/home/leni/Pop/repos/EpreuveDuFeu/s.txt"
s2 = ""
with open(s1) as f:
    s2 = f.read().splitlines()

for i in range(len(s2)):
    s2[i] = s2[i].replace("|", "")      #nettoyage des listes pour une meilleure manipulation par la suite
    s2[i] = s2[i].replace("_", "0")
s2.pop(3)
s2.pop(6)

#definition d'une grille de sudoku vide plus pour int tous les caractères
#Sinon conversion impossible.
sudoku=9*[0]
for i in range(len(sudoku)):
    sudoku[i]=9*[0]

#convertir les caracteres en entier
for i in range(0,9):
    for j in range(0,9):
        sudoku[i][j] = int(s2[i][j])
print(sudoku)



#Créer fonctions pour vérifier sudoku

def solve_sudoku(sudoku):
    i = 0
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]):
            if sudoku[i][j] == 0:
                new_value = 1
                while new_value < 10:
                    sudoku[i][j] = new_value
                    if check_line(sudoku, i) and check_column(sudoku, j) and check_square(sudoku, i, j):
                        
                    new_value+=1
                print(new_value)
            j+=1
    
        i+=1

solve_sudoku(sudoku)

    
            













#Créer une fonction principale pour vérifier les 3 secondaire
#rajouté les caractères spéciaux et print la liste

#Bien afficher le sudoku
#for i in range(0,9):
 #   print(sudoku[i])