class Car:
    def __init__(self, rekkari, maxvauhti, nykynopeus=0, valmatka=0):
        self.rekkari = rekkari
        self.maxvauhti = maxvauhti
        self.nykynopeus = nykynopeus
        self.valmatka = valmatka

    def kiihdytys(self, kiihdytys):
        if kiihdytys < 0:
            if self.nykynopeus + kiihdytys < 0: #pysähtyminen
                self.nykynopeus = 0
            else:
                self.nykynopeus += kiihdytys #vauhdinmuutoso

        elif self.nykynopeus + kiihdytys > self.maxvauhti: #ettei mene yli maksimin
            self.nykynopeus = self.maxvauhti

        else:
            self.nykynopeus += kiihdytys
        return self.nykynopeus

    def liike(self, tunnit):
        self.valmatka = self.valmatka + self.nykynopeus * tunnit

car1 = Car("ABC-123", 142)
car1.kiihdytys(30)
print(f"Auton nopeus: {car1.nykynopeus}")
car1.liike(1.5)
car1.kiihdytys(70)
print(f"Auton nopeus: {car1.nykynopeus}")
car1.kiihdytys(50)
print(f"Auton nopeus: {car1.nykynopeus}")
car1.kiihdytys(-200)
print(f"Auton nopeus: {car1.nykynopeus}")

print(f"Rekisterinumer {car1.rekkari}, Huippunopeus {car1.maxvauhti}, "
      f"Tämänhetkinen nopeus {car1.nykynopeus} km/h, Kuljettu matka {car1.valmatka}")