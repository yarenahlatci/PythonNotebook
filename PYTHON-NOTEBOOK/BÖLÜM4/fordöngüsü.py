#Döngüler

#for döngüsü, belirli bir dizi veya veri yapısı üzerinde işlem yapmak için kullanılır. Bu döngü, her bir elemanı sırayla alarak döngü bloğunu çalıştırır.
#for eleman in veri_yapısı:
    # Döngü bloğu


liste = [1, 2, 3, 4, 5]

for sayi in liste: #in listenin içinde gezinmek anlamında kullanılır
    print(sayi)


sehirler=["Ankara","İstanbul","İzmir"]
for gez in sehirler:
    print("Şehir:",gez)

for sehir in sehirler:
    if sehir == "Ankara":
        print(sehir + " için kod: "+ sehir[0:3])
print("*********") #Döngü dışında her zaman çalışacak


# while Döngüsü:
# while döngüsü, belirli bir koşul doğru olduğu sürece döngü bloğunu çalıştırmak için kullanılır.
#while koşul:
    # Döngü bloğu

sayac = 0
while sayac < 5:
    print(sayac)
    sayac += 1


sayac1 = 1
sonuc =0
while sayac1 <= 10:
    sonuc = sonuc + sayac1
    sayac1 = sayac1 + 1
print(sonuc)


"""
break ve continue ifadeleri:

break: Döngüyü aniden sonlandırmak için kullanılır.

continue: Döngünün geri kalanını atlayarak bir sonraki adıma geçmek için kullanılır.

"""
for sayi in range(10):
    if sayi == 5:
        break  # Döngüyü sonlandırır
    print(sayi)

    
for sayi in range(10):
    if sayi % 2 == 0:
        continue  # Tek sayıları atlar
    print(sayi)


"""
Range fonksiyonu ile çalışmak
range() fonksiyonu ardışık sayı dizileri oluşturmak için kullanılır. Genellikle for döngüleri ile birlikte kullanılır.
range(başlangıç, bitiş, adım)

"""

for i in range(5):
    print(i)  # 0'dan 4'e kadar sayıları yazdırır

for j in range(1, 10, 2):
    print(j)  # 1'den 9'a kadar tek sayıları yazdırır
