print("Geometrik Şekillerin Alanlarını Hesaplama")

def dikdortgen(kisaKenar, uzunKenar):
    print("Dikdörtgenin alanı = {}".format(kisaKenar * uzunKenar))

def kare(kenar):
    print("Karenin alanı = {}".format(kenar * kenar))

def yamuk(altTaban, ustTaban, yukseklik):
    print("Yamuğun alanı = {}".format(((altTaban + ustTaban) * yukseklik) / 2))

def eskenardortgen(altKenar, yanKenar):
    print("Eşkenar dörtgenin alanı = {}".format((altKenar * yanKenar) / 2))

def paralelkenar(altTaban, yukseklik):
    print("Paralel kenarın alanı = {}".format(altTaban * yukseklik))

if __name__ == '__main__':
    print("Geometrik Şekil Alan Hesaplama")
    print("1. Kare")
    print("2. Dikdörtgen")
    print("3. Yamuk")
    print("4. Paralel Kenar")
    print("5. Eşkenar Dörtgen")

    secim = int(input("Alanını hesaplamak istediğiniz şekli seçin: "))

    if secim == 1:
        k = int(input("Karenin bir kenarı: "))
        kare(k)

    elif secim == 2:
        kisaKenar = int(input("Dikdörtgenin kısa kenarı: "))
        uzunKenar = int(input("Dikdörtgenin uzun kenarı: "))
        dikdortgen(kisaKenar, uzunKenar)

    elif secim == 3:
        altTaban = int(input("Yamuğun alt taban uzunluğu: "))
        ustTaban = int(input("Yamuğun üst taban uzunluğu: "))
        yukseklik = int(input("Yamuğun yüksekliği: "))
        yamuk(altTaban, ustTaban, yukseklik)

    elif secim == 4:
        altTaban = int(input("Paralel kenarın alt taban uzunluğu: "))
        yukseklik = int(input("Paralel kenarın yüksekliği: "))
        paralelkenar(altTaban, yukseklik)

    elif secim == 5:
        altKenar = int(input("Eşkenar dörtgenin alt kenar uzunluğu: "))
        yanKenar = int(input("Eşkenar dörtgenin yan kenar uzunluğu: "))
        eskenardortgen(altKenar, yanKenar)

    else:
        print("Yanlış seçim yaptınız. Lütfen seçimi kontrol edin.")
