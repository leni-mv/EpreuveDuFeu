a = input("nombres : ")
a = list(a)
i = 0
flag = True

#j'ajouterais le booléen après
while flag == True:
    i = 0
    flag = False
    while i < (len(a)-1):
        if a[i] < a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
            flag = True
        i+=1
    
b = ""
for j in a :
    b+=j

print(b)