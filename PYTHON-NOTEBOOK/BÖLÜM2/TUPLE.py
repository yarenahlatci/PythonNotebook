#Tuple
# Listelere benzerdir. Tek farklı listelerde elemanları değiştirebiliyorken tupleda değiştiremezsiniz. Bu veri yapısı performanslı bir data sağlar

#Python'da "tuple", değiştirilemez (immutable) ve virgülle ayrılan elemanlardan oluşan bir veri yapısıdır. Listelerle benzerdir, ancak bir kez oluşturulduktan sonra içeriği değiştirilemez. Tuple, parantezler () içine alınarak oluşturulur ve elemanlarının sırası korunur.

# Tuple oluşturma
my_tuple = (1, 2, 3, "merhaba", True)

# Tuple'lar değiştirilemez olduğundan, elemanlarını sonradan eklemek, silmek veya değiştirmek mümkün değildir. Ancak, tuple içindeki verileri kullanmak ve erişmek mümkündür:
# Tuple elemanlarına erişim
print(my_tuple[0])  # Çıktı: 1
print(my_tuple[3])  # Çıktı: merhaba

#Python'da tuple'lar için özel fonksiyonlar yoktur, çünkü tuple'lar değiştirilemez olduğu için liste için kullanılan birçok fonksiyon tuple üzerinde de çalışır.

#len(): Tuple'ın eleman sayısını döndürür.
my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(length)  # Çıktı: 5

#count(): Belirtilen değerin tuple içinde kaç kez geçtiğini döndürür.
my_tuple = (1, 2, 3, 2, 4, 2, 5)
count = my_tuple.count(2)
print(count)  # Çıktı: 3

#index(): Belirtilen değerin tuple içindeki ilk indeksini döndürür.
my_tuple = (10, 20, 30, 20, 40)
index = my_tuple.index(20)
print(index)  # Çıktı: 1

# İç içe tuple oluşturma ve erişim 
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))

print(nested_tuple[0])        # Çıktı: (1, 2, 3)
print(nested_tuple[1][0])     # Çıktı: a
print(nested_tuple[2][1])     # Çıktı: False