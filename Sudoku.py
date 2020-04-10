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



#Créer fonctions pour vérifier sudoku
def init_array():
    new_array = 9*[0]
    val = 0
    while val < 9:
        new_array[val] = 9*[0]
    val+=1
    return new_array

def check_line(sudoku, i):
    print("l")
    array = init_array()
    j = 0
    while j < len(sudoku[i]):
        val = sudoku[i][j]
        if val > 0 and val < 10 :
            array[val]+=1
            if array[val] > 1:
                return False
        j+=1
    return True

def check_column(sudoku, j):
    print("c")
    array = init_array()
    i = 0
    while i < len(sudoku):
        val = sudoku[i][j]
        if val > 0 and val < 10 :
            array[val]+=1
            if array[val] > 1:
                return False
        i+=1
    return True

def check_square(sudoku, i, j):
    print("c")
    array = init_array()
    square_begin_i = (i/4)*4
    square_begin_j = (j/4)*4
    i = 0
    while i < (square_begin_i + 3):
        while j < (square_begin_j + 3):
            val = sudoku[i][j]
            if val > 0 and val < 10 :
                array[val]+=1
                if array[val] > 1:
                    return False
            j+=1
        i+=1
    return True

def solve_sudoku(sudoku):
    i = 0
    while i < len(sudoku):
        j = 0
        while j < len(sudoku[i]): #là il passe 8fois : est-ce les 0 du sudoku
            print("ok!")
            if sudoku[i][j] == 0: #là il passe une fois
                new_value = 1
                while new_value < 10:
                    sudoku[i][j] = new_value
                    if check_line(sudoku, i) and check_column(sudoku, j) and check_square(sudoku, i, j): #après cette ligne je ne sais
                        sudoku = solve_sudoku(sudoku)                                                    #pas comment vérifier mon code
                        if sudoku != False:
                            return sudoku                        
                    new_value+=1
                return False
            j+=1
        i+=1

solve_sudoku(sudoku)


#Bien afficher le sudoku
#for i in range(0,9):
 #   print(sudoku[i])