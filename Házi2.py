print("1.Feladat\n")

import math
def kör(r):
    print("Kör terület:",2*r*math.pi,"\n")
r=float(input("sugár:"))
kör(r)

def téglalap(a,b):
    print("Téglalap terület:",a*b,"\n")
a=float(input("a oldal:"))
b=float(input("b oldal:"))
téglalap(a,b)

def gúla(r,m):
    print("Gúla térfogat:",(r**2*math.pi*m)/3,"\n")
m=float(input("magasság:"))
gúla(r,m)

print("2.Feladat\n")

n=int(input("A keresett n-edik tag:"))
a=0
b=1
szám=0
count=1
print("N-edik helyen lévő szám: ")
while(count<=n):
  count+=1
  a=b
  b=szám
  szám=a+b
print(szám,"\n")

print("3.Feladat\n")
szám=input("Írj be egy egész számot:")
számjegyek=[]
for i in szám:
    számjegyek.append(i)
if számjegyek[0]==számjegyek[-1] and számjegyek[1]==számjegyek[-2] and számjegyek[2]==számjegyek[-3] and számjegyek[3]==számjegyek[-4]:
    print("A szám tükörszám\n")
else:
    print("A szám nem tükörszám\n")

print("4.Feladat\n")

def distance(p1, p2):
    print("A két pont távolsága:", math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2))
p1 = (1, 2)
p2 = (6, 5)
distance(p1, p2)
