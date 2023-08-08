#For döngüsü ile konsola istenilen yükseklikte çam ağacı çizmek.
height = int(input('Height: '))
leaves = height * 0.75
 
for x in range(height + 1):
    if x <= leaves: print((x * '*').center(height))
    else: print('||'.center(height))

#Yıldızlar çalışması
sayi = int(input("Kaç yıldız olsun?"))
yildiz = ""

for x in range(1,sayi + 1):
    yildiz = yildiz + "*"
    print(yildiz)

#Asal sayı hesaplama
deger = int(input("Sayı giriniz:"))
asalMi = "Evet!"

for x in range(2,deger):
    if(deger % x) == 0:
        asalMi = "Hayır!"
        break
if asalMi == "Evet!":
        print("Asal")
else:
        print("Asal değil!")