# 1 - Sayıların yerini değiştir
#X ve Y değişkenlerin değerlerini nasıl birbiriyle değiştirebiliriz?
#Temp geçiçi değişken tutacağız. X değerini temp değerine atadık. X ve Y değiştirdik. Daha sonra y temp değişkenin değerini atadık. Bu şekilde birbirlerinin değerleriyle değişmiş oldular.
x = 10
y = 20

temp = x
x = y
y = temp

print("x = " + str(x))
print("y = " + str(y))


#2 -Kaç kilometre kaç mil eder?

mil = 0.621371192
km = int(input("Kaç km?"))
donustur = (km * mil)
print(str(km)+ " km " + str(donustur)+" mil eder ") #Python'da, farklı veri tiplerini birleştirmek için metin (string) formatına dönüştürme işlemi yapılması gerekmektedir.

#Kod açıklamaları

# km = int(input("Kaç km?")): Kullanıcıdan bir giriş istenir ve bu giriş km değişkenine atılır. int() fonksiyonu ile kullanıcıdan alınan giriş sayıya dönüştürülür. Kullanıcının girdiği değer sayı olmadığı durumda hata verecektir. Eğer kullanıcıdan metin alınmak istenirse int() fonksiyonu kaldırılabilir.

# donustur = (km * mil): Bu satırda, girilen kilometre değeri ile mil değeri (dönüşüm oranı) çarpılarak mil cinsinden bir değer hesaplanır ve donustur değişkenine atılır.

# print(str(km)+ " km " + str(donustur)+" mil eder "): Bu satırda, print() fonksiyonu kullanarak sonucu ekrana yazdırıyoruz. Ancak, print() fonksiyonu yalnızca aynı veri türlerini birleştirebilir, bu nedenle sayı olan km ve donustur değişkenlerini metin (string) formatına dönüştürmemiz gerekiyor. Bunun için str() fonksiyonu kullanılıyor. Ardından + operatörü ile metinleri birleştirerek sonuç ekrana yazdırılır.