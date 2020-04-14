#!bin/python3.6
#14h21 #14h39 #18min et seule ! owo


n = input("Ecrit un chiffre :")
n = int(n)
m = n
i = 0
#d'abord les dièzes
while i < m:
    n-=1
    i+=1
    print(" " * n + "#" * i)

