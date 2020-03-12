#!/bin/python3.6

a = input("écris plein de nombres dans le désordre : ")
a = list(a)
n = 0

for i in a[0][0]:
    if i != str(n):
        continue
    elif i == str(n):
        print(i)
    n += 1