class Android:
    def __init__(self, versi, harga):
        self.versi = versi
        self.harga = harga
    
    def thn(self):
        print('2021')

class Iphone:
        def __init__(self, versi, harga):
            self.versi = versi
            self.harga = harga

        def thn(self):
            print('2021')

phone1 = Android("android 12", "1,5 juta ++")
phone2 = Iphone("IOS 16", "17 juta ++")

for hp in(phone1, phone2):
    hp.thn()