#Stringler = !!!!!Python büyük küçük harfe duyarlıdır.!!!!! "" ile tanımlanır.

#Substring
message = "Hello world" #0.indexten başlar
print(message)
print(message[2]) #2.indexi istedik. 0.indexten başlar. 
print(message[2:5]) #2.indexten başla 5.indexe kadar getir ama 5 dahil değil. En son yazdığınız hiç bir zaman dahil olmaz.
print(message[3:]) #3.indexten başla en sona kadar yaz. Hepsini ver demektir.
print(message[:2]) #En baştan başla 2.indexe kadar yaz ama 2.index dahil değil

#En son karaktere nasıl ulaşılır? Len fonksiyonu ile ulaşırız.
print(len(message)) #Kaç karakter olduğunu buluruz.
yeniMesaj = message[len(message)-1:len(message)] #En son harfi buluruz
print(yeniMesaj)

#Yazıyı nasıl tersten yazdırırız?
print(message[::-1])


#Lower & Upper Fonksiyonu
#Lower = Harfleri küçültmek için M -> m
#Upper = Harfleri büyültmek için m -> M 

text = "Yaren Ahlatcı"
print(text.upper()) #Çıktısı YAREN AHLATCI
print(text.lower()) # Çıktısı yaren ahlatcı

#Replace = REPLACE komutunu bir string veri içindeki istenilen alanın istenilen şekilde değiştirilmesi için kullanırız.
print(text.replace("a","e")) #A harflerini e harfine çevir. 

#Split & Strip = Strip metodu, karakter dizisinin baş ve sondaki boşluk karakterlerini siler. Split metodu liste haline getirir.
#Split
bilgi = "   Yaren Ahlatcı 22 İstanbul     "
print(bilgi.split()) #Liste haline getirir. Çıktısı ['Yaren', 'Ahlatcı', '22', 'İstanbul']

#Strip
print(bilgi.strip()) #Başta veya sondaki boşlukları siler.
username = "     yarenahlatcı     "
x = username.strip()
print("my username is",x)  # my username is sadikturan

#Eğer strip() metodunun belirttiğimiz karakterleri silmesini istersek bu karakteri parametre olarak göndermemiz gerekir.
username = ",,,,...!!yarenn***"
x = username.strip(',.!*')
print("my username is",x)  # my username is yarenn

#İnput = Kullanıcıdan bilgi almak için kullanılır

ad = (input("Adınızı girin: ").upper()) #Kullanıcının adını input ile alırız. Ben girilen adların büyük harfle gözükmesini istediğim için upper fonksiyonunuda ekledim.
yas = input("Yaşınızı girin: ")
print("Kullanıcının adı: ",ad + " " + "Kullanıcının yaşı: ",yas)

sayi1 = input("Sayi 1 = ?")
sayi2 = input("Sayi 2 = ?")
print("Toplamları:",int(sayi1) + int(sayi2)) #Kullanıcıdan alınan her bilgi string yapıdadır. Biz bunu int,float gibi dönüştürmemiz lazım.