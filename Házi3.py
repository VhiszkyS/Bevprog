print("Caesar kódolás\n")

kód="kwwsv=22|rxwx1eh2gTz7z<Zj[fT"
asd=[]
megfejtés=[]
for i in kód:
    asd.append(ord(i)-3)
for x in asd:
    megfejtés.append(chr(x))
print("Megfejtés:","".join(megfejtés),"\n")
#Azért a RickRoll csúnya dolog :(

print("Bizonyos karakterek\n")

def valid(text,chars):
    for x in text:
        for y in chars:
            if x==y:
                print(x,"\n")
text=input("Írj be valalmit:")
chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
valid(text,chars)

print("Beszúró függvény\n")

def szavak(szó1,szó2):
    print(szó2+" "+szó1,"\n")
szó1=input("Első szó:")
szó2=input("Második szó:")
szavak(szó1,szó2)

print("Bináris konverter\n")

def Bináris_konverter(Szám):
    if Szám>1:
        Bináris_konverter(Szám//2)
        print(Szám%2,end='')

Szám=int(input("Írj be egy decimális számmot:"))
Bináris_konverter(Szám)


