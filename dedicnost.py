import math

class Tvar:
    def __init__(self):
        print("Tvořím tvar")

class Ctverec(Tvar):
    def __init__(self, a=0):
        super().__init__()
        self.a = a
        print("Tvořím čtverec")

    def obvod(self):
        return self.a * 4

    def obsah(self):
        return self.a * self.a

    def ziskej_a(self):
        return self.a

    def info(self):
        print(f"čtverec o delce strany {self.a}")

class Obdelnik(Ctverec):
    def __init__(self, a=0, b=0):
        super().__init__(a)
        self.b = b
        print("Vytvářím obdelnik")

    def obvod(self):
        return 2 * self.b + 2 * self.ziskej_a()

    def obsah(self):
        return self.b * self.ziskej_a()

    def info(self):
        print(f"obdelnik so stranou delky {self.ziskej_a()} a druhou stranou delky {self.b}")

class Kocka(Ctverec):
    def __init__(self, a=0):
        super().__init__(a)
        print("Vytvářím kocku")

    def objem(self):
        return self.obsah() * self.ziskej_a()

    def info(self):
        print(f"Kocka so stranami delky {self.ziskej_a()}")

class Kruh(Tvar):
    def __init__(self, polomer=0):
        super().__init__()
        self.polomer = polomer
        print("Vytvářím kruh")

    def obvod(self):
        return 2 * math.pi * self.polomer

    def obsah(self):
        return math.pi * self.polomer ** 2

    def ziskej_polomer(self):
        return self.polomer

    def info(self):
        print(f"Kruh s polomerom {self.polomer}")

class Valec(Kruh):
    def __init__(self, polomer=0, vyska=0):
        super().__init__(polomer)
        self.vyska = vyska
        print("Vytvářím valec")

    def objem(self):
        return math.pi * self.ziskej_polomer() ** 2 * self.vyska

    def info(self):
        print(f"Valec s polomerom {self.ziskej_polomer()} a výškou {self.vyska}")

class Koule(Kruh):
    def __init__(self, polomer=0):
        super().__init__(polomer)
        print("tvořím kouly")

    def objem(self):
        return (4 / 3) * math.pi * self.ziskej_polomer() ** 3

    def info(self):
        print(f"Koule s polomerom {self.ziskej_polomer()}")

if __name__ == "__main__":
    rec = Obdelnik()
    rec1 = Obdelnik(5, 6)
    kc = Kocka(5)
    print(kc.objem())
    kc.info()

    kr = Kruh(3)
    print(kr.obvod())
    print(kr.obsah())
    kr.info()

    val = Valec(3, 4)
    print(val.objem())
    val.info()

    gul = Koule(2)
    print(gul.objem())
    gul.info()
