#Pozitif mi negatif mi?

sayi1 = int(input("Lütfen bir sayı giriniz: "))

if sayi1 == 0:
    print("Girilen sayı 0")
elif sayi1 > 0:
    print("Sayı pozitif.Girilen sayı: ",sayi1)
else:
    print("Sayi negatif. Girilen sayı: ",sayi1)


#En büyük sayı hangisi?

print("Merhaba!")
deger1 = int(input("1.sayıyı giriniz:"))
deger2 = int(input("2.sayıyı giriniz:"))
deger3 = int(input("3.sayıyı giriniz:"))

if (deger1>= deger2) and (deger1 >= deger3):
    print("En büyük sayı: ",deger1)
elif (deger2 >= deger1) and (deger2>= deger3):
    print("En büyük sayı: ",deger2)
else:
    print("En büyük sayı: ",deger3)