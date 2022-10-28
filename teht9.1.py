class Car:
    def __init__(self, rekkari, maxvauhti, nykynopeus=0, valmatka=0):
        self.rekkari = rekkari
        self.maxvauhti = str(maxvauhti) + " km/h"
        self.nykynopeus = str(nykynopeus) + " km/h"
        self.valmatka = valmatka

car1 = Car("ABC-123", 142)

print(f"Rekisteritunnus {car1.rekkari}, huippunopeus {car1.maxvauhti}, hetkellinen nopeus "
      f"{car1.nykynopeus}, kuljettu matka {car1.valmatka}")