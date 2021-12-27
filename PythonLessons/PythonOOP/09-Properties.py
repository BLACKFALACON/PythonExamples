class Personel():

    def __init__(self, isim, soyisim, departman):
        self.isim       = isim
        self.soyisim    = soyisim
        self.departman  = departman

    @property
    def bilgi(self):
        return F'İsim: {self.isim}, Soyisim: {self.soyisim}, Departman:{self.departman}'

    @bilgi.setter
    def bilgi(self,yeni_departman):
        self.departman = yeni_departman

    @bilgi.deleter
    def bilgi(self):
        del self.isim

personel_1 = Personel("Ömer", "Demirarslan", "Yazılım")

print(personel_1.bilgi)

personel_1.departman = "İK"

print(personel_1.bilgi)

del personel_1.isim

print(personel_1.bilgi)