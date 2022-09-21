print("1.Feladat\n")
kor=int(input("Életkor:"))
if kor>=21:
    print("Amerikában legálisan fogyaszthat már alkoholt, már vásárolhat dohányterméket Magyarországon, már szerezhet jogosítványt, és már megnézheti egyedül a Shrek 2-t")
elif kor>=18:
    print("Már vásárolhat dohányterméket Magyarországon, már szerezhet jogosítványt, és már megnézheti egyedül a Shrek 2-t")
elif kor>=16:
    print("Már szerezhet jogosítványt, és már megnézheti egyedül a Shrek 2-t")
elif kor>=12:
    print("Már megnézheti egyedül a Shrek 2-t")
else:
    print("Még mindenhez túl fiatal :(\n")

print("2.Feladat\n")
import math
print("Pitagorasz-tétel")

a=float(input("a oldal:"))
b=float(input("b oldal:"))
if a>0 and b>0:
    c=a**2+b**2
    c=math.sqrt(c)
    print("a oldal:",a," b oldal:",b," c oldal:",c,"\n")
else:
    print("Nincs ilyen háromszög")


print("Henger térfogata")

r=float(input("sugár:"))
m=float(input("magasság:"))
print("Térfogat:",r*r*math.pi*m,"\n")

print("Másodfokú egyenelet")

a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))
x1=(-b-math.sqrt(b**2-4*(a-c)))/2*a
x2=(-b+math.sqrt(b**2-4*(a-c)))/2*a
print("Megoldások:",x1,"és",x2,"\n")

print("3.Feladat\n")
nátrium=int(input("Nátrium:"))
klór=int(input("Klór:"))
nacl=0
FeleslegesNa=0
FeleslegesCl=0
if nátrium==klór:
    nacl=(nátrium+klór)*2
elif nátrium>klór:
    nacl=(nátrium+klór)*2
    FeleslegesNa=(nátrium-klór)*2
else:
    nacl=nátrium
    FeleslegesCl=(nátrium+klór)*2-nátrium
print("Létrejött konyhasó:",nacl," maradék nátriumatom:",FeleslegesNa," maradék klóratom:",FeleslegesCl)