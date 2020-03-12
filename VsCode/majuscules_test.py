
a = input("Ecris ce que tu veux : ")
b = a.split()

for i in b:
    if i == b[0][0::2]:
        print(i.upper())
    elif i == b[0][1::2]:
        print(i.lower())
    else:
        print("ça marche toujours pas ><")