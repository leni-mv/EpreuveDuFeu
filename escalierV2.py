#!/bin/python3.6

n = input("Nombre de marche ici : ")
n = int(n)
a = 0

while a < n:
    print(" " * (n-a), "#" * a)
    a = a + 1