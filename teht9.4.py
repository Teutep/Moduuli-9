import random
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

kilpailijat = []
for count in range(10):
    car = Car("ABC-" + str(count), random.randint(100,200))
    kilpailijat.append(car)

kilpailumenossa = 1
while kilpailumenossa:
    for cars in kilpailijat:
        cars.kiihdytys(random.randint(-10, 15))
        cars.liike(1)
        if cars.valmatka >= 10000:
            kilpailumenossa = 0

for cars in kilpailijat:
    print(f"{cars.rekkari}, {cars.maxvauhti}, {cars.nykynopeus}, {cars.valmatka}")