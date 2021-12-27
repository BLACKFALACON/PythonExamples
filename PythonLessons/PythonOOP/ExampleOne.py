import datetime
class BikeRental: 
    def __init__(self,stock=0):
        """
        Bisiklet kiralama mağazasını somutlaştıran yapıcı sınıfımız.
        """
        self.stock = stock 
    def displaystock(self):
        """
       Mağazada şu anda kiralanabilen bisikletleri görüntüler.
        """
        print("We have currently {} bikes available to     rent.".format(self.stock))
        return self.stock
    def rentBikeOnHourlyBasis(self, n):
        """
        Bir müşteriye saatlik olarak bisiklet kiralar.
        """
        # reject invalid input 
        if n <= 0:
            print("Bisiklet sayısı pozitif olmalıdır!")
            return None
        # do not rent bike is stock is less than requested bikes
        
        elif n > self.stock:
            print("Üzgünüm! Şu anda kiralık {} bisikletimiz var.".format(self.stock))
            return None
        # rent the bikes        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bike(s) on hourly basis today at {} hours.".format(n,now.hour))
            print("Bisiklet başına her gün için 5$ ücretlendirilirsiniz.")
            print("Hizmetimizden memnun kalacağınızı umuyoruz.")
            self.stock -= n
            return now      
     
    def rentBikeOnDailyBasis(self, n):
        """
       Bir müşteriye günlük olarak bisiklet kiralar.
        """
        
        if n <= 0:
            print("Bisiklet sayısı pozitif olmalıdır!")
            return None
        elif n > self.stock:
            print("Üzgünüm! Şu anda kiralık {} bisikletimiz var.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} bike(s) on daily basis today at {} hours.".format(n, now.hour))
            print("Bisiklet başına her gün için 20 $ ücretlendirilirsiniz.")
            print("Hizmetimizden memnun kalacağınızı umuyoruz.")
            self.stock -= n
            return now
        
    def rentBikeOnWeeklyBasis(self, n):
        """
       Bir müşteriye haftalık olarak bisiklet kiralar.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        elif n > self.stock:
            print("Üzgünüm! Şu anda kiralık {} bisikletimiz var.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("Bisiklet başına her hafta için 60 $ tahsil edilecektir.")
            print("Hizmetimizden memnun kalacağınızı umuyoruz.")
            self.stock -= n
            return now
    
    
    def returnBike(self, request):
        """
        1. Bir müşteriden kiralık bisikleti kabul edin
        2. Envanteri doldurur
        3. Bir faturayı iade edin
        """
       
        # demeti çıkar ve faturayı başlat
        rentalTime, rentalBasis, numOfBikes = request
        bill = 0
        # sadece üç parametrenin tümü boş değilse bir fatura düzenleyin!
        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # saatlik fatura hesaplama
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 5 * numOfBikes
                
           # günlük fatura hesaplama
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 20 * numOfBikes
                
            # haftalık fatura hesaplama
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 60 * numOfBikes
            
           # aile indirimi hesaplaması
            if (3 <= numOfBikes <= 5):
                print("%30 indirimli Aile kiralama promosyonu için uygunsunuz")
                bill = bill * 0.7
            print("Bisikletini geri verdiğin için teşekkürler. Umarım hizmetimizden memnun kalmışsınızdır!")
            print("That would be ${}".format(bill))
            return bill
        
        else:
            print("Bizimle bisiklet kiraladığınızdan emin misiniz?")
            return None
class Customer:
    def __init__(self):
        """
        Çeşitli müşteri nesnelerini somutlaştıran yapıcı yöntemimiz.
        """
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0
    
    def requestBike(self):
        """
        Müşteriden bisiklet sayısı için bir talep alır.
        """
                      
        bikes = input("How many bikes would you like to rent?")
        
        # geçersiz giriş için mantık uygula
        try:
            bikes = int(bikes)
        except ValueError:
            print("That's not a positive integer!")
            return -1
        if bikes < 1:
            print("Geçersiz Giriş. Bisiklet sayısı sıfırdan büyük olmalıdır!")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
        """
       Müşterilerin bisikletlerini kiralık dükkana iade etmelerini sağlar.
        """
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0