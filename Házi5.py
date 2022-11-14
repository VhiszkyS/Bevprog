#Pi vers
txt=[]
with open ("pi_vers.txt", "r") as f:
    for i in f:
        txt.append(i)
f.close()
with open ("pi_elsoszamjegy.txt", "w") as f2:
    for x in txt:
        x=x.split(' ')
        print('A pi első számjegye: ',len(x[0]),file=f2)
f2.close()

#Fájlkezelés
with open("string1.txt", "r") as bemenet:
    with open("string1_clean.txt", "w") as kimenet:
        for i in bemenet:
            if '#' not in i:
                kimenet.write(i)
bemenet.close()
kimenet.close()