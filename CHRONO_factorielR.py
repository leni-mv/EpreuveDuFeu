#calculer la factoriel de n'importe quel nombre
#Entre 15h35 et 15h41

n = input("Calcule la super factoriel de :")
n = int(n)

if n > 1:
    print(n*(n-1))
else:
    print(n)


