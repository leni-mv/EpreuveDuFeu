#!/bin/python3.6

n = input("Calculer la factoriel de : ")
n = int(n)
print(n)
def fact(n):
    if n < 2:
        return 1
    else:
        return n*fact(n-1)

print(fact(n))