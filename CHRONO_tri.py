#Ttrier n'importe quelle liste d'élément, résolu en 1h + 20min de pause.

éléments = input("nombres :")
élément = []
for nombre in éléments:
    élément += nombre


for i in élément:                          #passer autant de fois qu'il y a de chiffres
    i = 0                                  #reboot i et x pour trier à chaque passages
    x = 1
    if i < x:                              #Condition pour repérer ce qui est non trié encore
        while x < len(élément):            #Condition pour faire le tri sur toute la ligne
            if élément[i] < élément[x]:    #tri pur
                tmp = élément[i]
                élément[i] = élément[x]
                élément[x] = tmp
            i+=1
            x+=1
            élément = élément
    else:
        i+=1
        x+=1

resultat = ""
for n in élément:
    resultat += n
print(resultat)
