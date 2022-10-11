class Fejlesztők:
    def __init__(self,nev,fizetes,rang='Junior',bedolgozott_ev=0)->None:
        self.dupont=1000
        self.nev=nev
        self.fizetes=fizetes
        self.rang=rang
        self.bedolgozott_ev=bedolgozott_ev
    def emeles(self,megemelt_fizu=10000):
        self.fizetes+=megemelt_fizu
    def fejlesztoi_evek(self,plusz_ev=1):
        self.bedolgozott_ev+=plusz_ev
    def fejleszto_rangja(self,fejleszto_ev=0):
        fejleszto_ev=self.bedolgozott_ev
        if fejleszto_ev==0:
            self.rang='Intern'
        elif 1<=fejleszto_ev<=2:
            self.rang="Junior"
        elif 2<fejleszto_ev<=5:
            self.rang="Medior"
        else:
            self.rang="Senior"

    def kiir(self):
        print("Név: {0}, Fizetés: {1}, Rang: {2}, Fejlesztői év: {3}".format(self.nev, self.fizetes, self.rang, self.bedolgozott_ev))

Fejleszto1=Fejlesztők('Géza',45000,'Junior',5)
Fejleszto1.emeles()
Fejleszto1.fejlesztoi_evek()
Fejleszto1.fejleszto_rangja()
Fejleszto1.kiir()
