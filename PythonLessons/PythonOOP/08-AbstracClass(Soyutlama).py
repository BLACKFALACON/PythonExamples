from abc import ABC, abstractmethod

class Oyuncular(ABC):
    def __init__(self, isim, soyisim, takim):
        self.isim    = isim
        self.soyisim = soyisim
        self.takim   = takim

    @abstractmethod
    def saglik(self):
        return 100

    @abstractmethod
    def bomba_kullan(self):
        print("Bomba atıyorum")

class Dusman(Oyuncular):
    def __init__(self, isim, soyisim, takim, silah):
        super().__init__(isim, soyisim, takim)
        self.silah = silah

    def saglik(self):
        return 100

    def bomba_kullan(self):
        print("Bomba Atıyorum")

class Dost(Oyuncular):
    def __init__(self, isim, soyisim, takim, silah):
        super().__init__(isim, soyisim, takim)
        self.silah = silah

    def saglik(self):
        return 100

    def bomba_kullan(self):
        print("Bomba Atıyorum")

dusman_1 = Dusman("Mert", "Kaya", "Dusman", "AK-47")
print(dusman_1.silah)
print(dusman_1.takim)
print(dusman_1.saglik())
print(dusman_1.bomba_kullan())

dost_1 = Dost("Salid", "Hakiki", "Dost", "MPT-76")
print(dost_1.silah)
print(dost_1.takim)
print(dost_1.saglik())
print(dost_1.bomba_kullan())