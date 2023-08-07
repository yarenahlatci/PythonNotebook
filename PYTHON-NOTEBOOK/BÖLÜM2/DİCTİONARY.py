"""
Dictionary (sözlük), Python'da anahtar-değer (key-value) çiftleri ile temsil edilen bir veri yapısıdır. Sözlükler, herhangi bir veri tipinden anahtarlarla ilişkilendirilmiş değerleri tutarlar. Anahtarlar benzersiz olmalıdır ve değiştirilemez (immutable) veri tipleri olmalıdır (örneğin, sayılar, metinler, tuple'lar).

Sözlükler, veriye hızlı erişim sağlar ve veri üzerinde etkili bir şekilde işlem yapma imkanı sunar. Sözlükler, süslü parantezler {} içine alınarak oluşturulur ve anahtar ve değerler arasında iki nokta üst üste ":" ile ayrılır.

"""

#Sözlük oluşturma ve eleman ekleme:
# Sözlük oluşturma
student = {
    "name": "Yaren",
    "age": 22,
    "department": "Computer Programmer"
}

# Sözlüğe yeni eleman ekleme
student["email"] = "yaren@example.com"
print(student)
# Çıktı: {'name': 'Yaren', 'age': 22, 'department': 'Computer Programmer', 'email': 'yaren@example.com'}

#Sözlük üzerinde erişim
# Sözlük üzerinde anahtarlarla erişim
print(student["name"])        # Çıktı: Yaren
print(student["age"])         # Çıktı: 22
print(student.get("email"))   # Çıktı: yareb@example.com

#Sözlük değerlerini değiştirme:
student["age"] = 26
print(student["age"])  # Çıktı: 26

#Sözlükte gezinme (iteration):
for key, value in student.items():
    print(key, ":", value)

# Çıktı:
# name : Yaren
# age : 26
# department : Computer Programmer
# email : yaren@example.com

#Sözlükte anahtarları ve değerleri almak:
keys = student.keys()
values = student.values()

print(keys)    
print(values)  

# Çıktı:
# dict_keys(['name', 'age', 'department', 'email'])
# dict_values(['Yaren', 26, 'Computer Programmer', 'yaren@example.com'])