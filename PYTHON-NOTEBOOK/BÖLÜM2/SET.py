#Listelere benzerdir. En önemli özelliği indexsiz ve sırasız elemanlardan oluşması. Veri tekrarı söz konusu olamaz. Tüm elemanlar eşssizdir. 

# Python'da "set", benzersiz ve sırasız elemanlardan oluşan bir veri yapısıdır. Setler, küme mantığına dayanır ve her bir elemanı yalnızca bir kez içerebilir. Setlerde elemanların sırası önemli değildir ve indekslenemezler.

# Setler, süslü parantezler {} veya "set()" fonksiyonu kullanılarak oluşturulabilir. Eğer set oluştururken süslü parantezler kullanıyorsanız, elemanlar arasında virgülle ayrılmaları gerekir. Setlerdeki elemanlar, veri türleri arasında karışık olabilir ve setler içinde başka bir set veya liste de bulunabilir.

#Set oluşturma ve eleman ekleme:
# Süslü parantezlerle set oluşturma
my_set = {1, 2, 3, 4, 5}

# set() fonksiyonu ile set oluşturma
another_set = set([3, 4, 5, 6, 7])

print(my_set)       # Çıktı: {1, 2, 3, 4, 5}
print(another_set)  # Çıktı: {3, 4, 5, 6, 7}

#Set'e eleman ekleme ve çıkarma:
my_set = {1, 2, 3}

# Eleman ekleme
my_set.add(4)
print(my_set)  # Çıktı: {1, 2, 3, 4}

# Eleman çıkarma
my_set.remove(2)
print(my_set)  # Çıktı: {1, 3, 4}

#update(): Bu metod, bir sete diğer bir seti veya başka bir iterable (örneğin liste veya tuple) veri tipini eklemek için kullanılır. Elemanlar tekrarlanmaz, yani sadece benzersiz elemanlar eklenir.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # Çıktı: {1, 2, 3, 4, 5}

list1 = [6, 7, 8]
set1.update(list1)
print(set1)  # Çıktı: {1, 2, 3, 4, 5, 6, 7, 8}

#discard(): Bu metod, bir setten belirtilen elemanı çıkarmak için kullanılır. Eğer eleman sette yoksa, herhangi bir hata vermez.
my_set = {1, 2, 3, 4, 5}
my_set.discard(3)
print(my_set)  # Çıktı: {1, 2, 4, 5}

my_set.discard(6)  # sette 6 elemanı yok, hata vermez.

#pop(): Bu metod, bir setten rastgele bir elemanı çıkartır ve bu elemanı döndürür. Setler sırasız olduğu için hangi elemanın çıkacağı belli değildir.
my_set = {1, 2, 3, 4, 5}
popped_element = my_set.pop()
print(popped_element)  # Rastgele bir eleman, örneğin 3 (Çıktı değişebilir)

print(my_set)  # Çıktı: {1, 2, 4, 5}

#clear(): Bu, bir veri yapısının içeriğini tamamen boşaltmak için kullanılır. Örneğin, bir liste, tuple veya setin içindeki tüm elemanları kaldırmak için clear() yöntemi kullanılır.
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # Çıktı: []

#del: Bu ifade, bir değişkeni veya bir veri yapısının tamamını silmek için kullanılır. del ifadesini kullanarak bir değişkeni silebilir veya bir liste, tuple veya seti yok edebilirsiniz.
x = 10
del x
# x artık tanımlı değil ve hata verecektir.
# print(x)  # Hata: NameError: name 'x' is not defined

my_list = [1, 2, 3, 4, 5]
del my_list
# my_list artık yok edildi ve hata verecektir.
# print(my_list)  # Hata: NameError: name 'my_list' is not defined

"""
Farkları şöyle özetleyebiliriz:

clear(): Bir veri yapısının içeriğini siler, ancak veri yapısını kendisi silmez. Yani, boşaltılan liste, tuple veya set hala mevcut olacaktır.

del: Bir değişkeni veya bir veri yapısını (liste, tuple veya set) tamamen yok eder. Bu işlem sonrasında, değişken kullanılamaz veya veri yapısına erişilemez hale gelir.
"""

#Set işlemleri (birleşim, kesişim, fark):
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Birleşim = Birleşim (Union), iki veya daha fazla kümenin elemanlarının toplamını içeren yeni bir küme oluşturur. Her eleman yalnızca bir kez eklenir, yani tekrarlayan elemanlar yalnızca bir kere temsil edilir.
union_set = set1.union(set2)
print(union_set)  # Çıktı: {1, 2, 3, 4, 5}

# Kesişim = Kesişim (Intersection), iki veya daha fazla kümenin ortak elemanlarını içeren yeni bir küme oluşturur.
intersection_set = set1.intersection(set2)
print(intersection_set)  # Çıktı: {3}

# Fark = (Difference) Fark, bir kümeden diğer kümenin elemanlarını çıkararak yeni bir küme oluşturur.
difference_set = set1.difference(set2)
print(difference_set)  # Çıktı: {1, 2}

#Set ile döngü
my_set = {1, 2, 3, 4, 5}

for element in my_set:
    print(element)

# Yukarıdaki örnekte, set içindeki elemanları tek tek döngü kullanarak alıyoruz ve ekrana yazdırıyoruz. Ancak, setler sırasız olduğu için elemanların sırası garanti edilmez.

setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)
print(setA.union(setB))
print(setB.union(setA))

print(setA & setB)
print(setA.intersection(setB))
print(setB.intersection(setA))

print(setA - setB)
print(setA.difference(setB))
print(setB.difference(setA))

print(setA ^ setB)
print(setA.symmetric_difference(setB))
print(setB.symmetric_difference(setA))