#!/bin/python3.6

n = input("Nombre de marche ici : ")
n = int(n)
b = "#"
a = 0

while a < n:
    print("{:>20s}".format(b))
    a = a + 1
    b = b + "#"
   