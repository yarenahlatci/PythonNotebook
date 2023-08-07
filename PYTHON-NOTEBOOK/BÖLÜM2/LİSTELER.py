#Listeler = Listeler sıralı ve indexli bir yapıya sahiptir.

#Boş liste
bosListe = []
my_intList = [1,2,3,4,5]
my_strList = ["Yaren","Yeşim","Umut"]
my_mixList = [1,"Hello",3.4]

print(my_intList)
print(my_strList)
print(my_mixList)

ogrenciler = ["Yaren","Derin","Nisa"]

print(ogrenciler)
print(ogrenciler[0]) #Öğrenciler listenin 0.elemanını al yani "Yaren gelir"
print(ogrenciler[1])
print(ogrenciler[2])

#Listeye yeni eleman eklemek için append methodu kullanılır
ogrenciler.append("Ahmet")
print(ogrenciler)

#Listeden eleman silmek için remove methodu kullanırız
ogrenciler.remove("Derin")
print(ogrenciler)

ogrenciler[2] = "Sıla" #Öğrenciler listesindeki 2.indexteki elemanı sıla olarak değiştirir
print(ogrenciler)

#List constructor, listeleri bu şekilde de tanımlayabiliriz.
sehirler =list(("ankara","istanbul","ankara","ankara"))
print(sehirler)

#Liste Fonksiyonları
# len(): Listenin eleman sayısını döndürür.
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print(length)  # Çıktı: 5

#append(): Listenin sonuna yeni bir eleman ekler.
fruits = ["elma", "armut", "çilek"]
fruits.append("muz")
print(fruits)  # Çıktı: ['elma', 'armut', 'çilek', 'muz']

#remove(): İlk bulduğu belirtilen değeri listeden kaldırır.
numbers = [10, 20, 30, 20, 40]
numbers.remove(20)
print(numbers)  # Çıktı: [10, 30, 20, 40]

#count(): Belirtilen değerin listede kaç kez geçtiğini döndürür.
print("Ankara sayısı: " + str(sehirler.count("ankara"))) #Çıktısı Ankara sayısı: 3

#index(): Belirtilen değerin ilk bulunduğu indeksi döndürür.
print("İstanbul indexi: " + str(sehirler.index("istanbul"))) #Çıktısı İstanbul indexi: 1

#pop(): Belirtilen indeksteki elemanı listeden çıkarır ve bu elemanı döndürür.
fruits = ["elma", "armut", "çilek"]
popped_fruit = fruits.pop(1)
print(fruits)       # Çıktı: ['elma', 'çilek']
print(popped_fruit) # Çıktı: armut

#insert(): Belirtilen indekse yeni bir eleman ekler.
fruits = ["elma", "armut", "çilek"]
fruits.insert(1, "muz")
print(fruits)  # Çıktı: ['elma', 'muz', 'armut', 'çilek']

#Reverse
sehirler.reverse()
print(sehirler)

#Copy
sehirler3 = sehirler.copy() #Sehirler listesini sehirler3 değişkenine kopyaladık
print(sehirler3)

#extend(): Başka bir listenin elemanlarını mevcut liste ile birleştirir.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  # Çıktı: [1, 2, 3, 4, 5, 6]

#sort(): Listeyi sıralar (küçükten büyüğe veya büyükten küçüğe).
sehirler.sort()
print(sehirler)

#Reverse = Tersten Z - A sıralayabiliriz
sehirler.sort()
sehirler.reverse()
print(sehirler)

#"clear()" bir Python listesi üzerinde çağrıldığında, listenin içeriğini tamamen boşaltan bir liste metodu veya fonksiyonudur. Yani, listedeki tüm elemanları kaldırarak boş bir liste elde edersiniz.
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Çıktı: [1, 2, 3, 4, 5]
numbers.clear()
print(numbers)  # Çıktı: []
