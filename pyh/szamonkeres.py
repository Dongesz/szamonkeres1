#1.feladat
'''vez = input("add meg a vezetek neved!")
ker = input("add meg a kereszt neved!")

print(f"Üdvözöllek {vez} {ker}")
print(f"Üdvözöllek {ker} {vez} ")
'''
#2.feladat
'''
szam = int(input('adj meg egy szamot!'))
print(szam -1)
print(szam +1)
'''
#3.feladat
'''
szam1 = int(input('adj meg egy szamot!'))
szam2 = int(input('adj meg meg egy szamot!'))

print(szam1+szam2)
print(szam1-szam2)
print(szam1*szam2)
print(szam1/szam2)
'''
#4.feladat
'''
a = int(input("adj meg egy szamot!"))
b = int(input("adj egy masik szamot!"))
c = 2*a+3*b
print(c)
d = c-2*a-3*b
print(d)
'''
#5.feladat a,
'''
import random
list = []

for x in range (20):
    n = random.randint(1,12)
    list.append(n)

    if n % 2 == 0:
        print(n)
'''
#5.feladat b,
import random
list = []

for x in range (20):
    n = random.randint(1,12)
    list.append(n)

    if n % 2 != 0:
        print(n)
