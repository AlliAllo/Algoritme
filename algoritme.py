


class number:
    def __init__(self,number):
        self.number = number

    def primtal(self):
        # CHECK OM TALLET ER ET PRIMTAL
        # SHOUTOUT TIL GEEKFORGEEKS, DE HJALP MED KODEN TIL AT FINDE PRIMTALLET ;))
        # https://www.geeksforgeeks.org/python-program-to-check-whether-a-number-is-prime-or-not/

        if self.number == 1:
            print("Dumt sprøgsmål...")
        elif self.number == 2:
            print("Ved du hvad et primtal er?")
        elif self.number == 3:
            print("Prøv at skriv 5")
        elif self.number == 5:
            print("Fint, du vinder, ja, 1,2, 3 og 5 er primtal...")
        else:
            for num in range(2,self.number//2):
                if (self.number % num) == 0:
                    print(self.number,"er ikke et primtal")
                    break
                else:
                    print(self.number,"er et primtal")
                    break

    def tal(self):
        #CHECK OM TALLET ER LIGE ELLER ULIGE
        if (self.number % 2) == 0:
            print("Det er et lige tal")
        else:
            print("Det er et ulige tal")


def tekst():
    Number = (input("Indtast et tal "))
    try:
        Number = int(Number)
    except:
        print("Indtast et heltal...")
        tekst()
    else:
        x = number(Number)
        x.primtal()
        x.tal()
tekst()