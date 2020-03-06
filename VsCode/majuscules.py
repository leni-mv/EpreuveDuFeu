#!/bin/python3.6

a = input("Ecris ce que tu veux : ")

a = a.split()
b = a[0::2]
c = a[1::2]

b = str(b)
c = str(c)
b = b.upper()
c = c.lower()
d = b + c

print(d)