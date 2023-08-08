#KARAR YAPILARI = Python'da "if-else" ifadesi, belirli bir koşulun doğru veya yanlış olmasına bağlı olarak farklı kod bloklarının çalıştırılmasını sağlayan bir yapıdır. 
# İF - ELİF - ELSE

print("Merhaba !")
num = int(input("Lütfen sayı girin:"))

if num>0:
    print("Positive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")
############################################
#Temel If-Else Yapısı:
# if koşul:
    # Koşul doğru ise bu blok çalışır
# elif koşul:
     # Koşul doğru ise bu blok çalışır
# else:
    # Koşul yanlış ise bu blok çalışır

############################################
#Örnek 1: Sayı Karşılaştırma
x = 10
y = 5

if x > y:
    print("x, y'den büyük.")
else:
    print("x, y'den küçük veya eşit.")

############################################

# Örnek 2: Kullanıcıdan Girdi Alma
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print("Girilen sayı çift.")
else:
    print("Girilen sayı tek.")

############################################

#Örnek 3: Birden Fazla Koşul
not_ortalamasi = float(input("Not ortalaması girin: "))

if not_ortalamasi >= 90:
    print("Notunuz AA")
elif not_ortalamasi >= 80:
    print("Notunuz BA")
elif not_ortalamasi >= 70:
    print("Notunuz BB")
elif not_ortalamasi >= 60:
    print("Notunuz CB")
elif not_ortalamasi >= 50:
    print("Notunuz CC")
else:
    print("Dersten başarısız oldunuz.")

#Trafik Işıkları
lights = ["red","yellow","green"]
currentLight = lights[0]

if currentLight == 'red':
    print("STOP!")
elif currentLight == 'yellow':
    print("READY!")
else:
    print("GO!")

"""
OPERATÖRLER
"and" operatörü, birkaç koşulun aynı anda doğru olması durumunda toplu bir doğruluk değeri döndürmek için kullanılır.

if koşul1 and koşul2:
    # Her iki koşul da doğruysa bu blok çalışır

"or" operatörü, en az bir koşulun doğru olması durumunda toplu bir doğruluk değeri döndürmek için kullanılır.

if koşul1 or koşul2:
    # En az bir koşul doğruysa bu blok çalışır

not Operatörü:
"not" operatörü, bir koşulu tersine çevirmek için kullanılır. Eğer koşul doğruysa "False" döner, eğer koşul yanlışsa "True" döner.
x = 5
y = 10

if not x > y:
    print("x, y'den büyük değil.")

    
Karşılaştırma Operatörleri:
Karşılaştırma operatörleri, iki değeri karşılaştırmak için kullanılır ve genellikle "if" ifadesi içinde koşulları değerlendirmede kullanılırlar.

==: Eşit mi?
!=: Eşit değil mi?
>: Büyük mü?
<: Küçük mü?
>=: Büyük veya eşit mi?
<=: Küçük veya eşit mi?
    
"""