#trier liste d'éléments n'importe laquelle
#gérer la donner pour la int et liste ou argv[i]
#15h43 #16h10 je ne sais pas comment placer le flag pour ne pas avoir d'erreurs
#16h11-16h35 pause
#trouver un moyen de répéter l'opération autant de fois que néscessaire
#17h08 SANS REGARDER !! I'M BG !!!
#17h08-17h26 test dans le terminal ET ajout des lignes 10-13 (pour mettre chiffres que l'on veut) et 32-35 (pour une sortie plus jolie ^^)
#1h pile pour résoudre l'énoncé + 18min (de glande) pour rendre ça jolie et exécutable dans le terminal

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