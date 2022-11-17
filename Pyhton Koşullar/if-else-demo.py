# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 

# isim = input("isim : ")
# yas = int(input("yas : "))
# egitim = input("eğitim : ")

# if yas >= 18:
#     if (egitim == "lise") or (egitim == "üniversite"):
#         print(f"ehliyet alabilirsin {isim}")
#     else:
#          print("ehliyet alamazsın")
# else:
#     print("yaşın küçük")        




# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0-24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

# sınav1 = float(input("1. sınav : "))
# sınav2 = float(input("2. sınav : "))

# ortalama = (sınav1 + sınav2)*0.5

# if (ortalama < 25) and (ortalama >= 0):
#     print("notunuz 0")
# elif (ortalama < 45)  and (ortalama > 24):
#     print("notunuz 1")
# elif (ortalama < 55)  and (ortalama > 44):
#     print("notunuz 2")
# elif (ortalama < 70)  and (ortalama > 54):
#     print("notunuz 3")
# elif (ortalama < 85)  and (ortalama > 69):
#     print("notunuz 4")
# elif (ortalama <= 100)  and (ortalama > 84):
#     print("notunuz 5")
# else:
#     print("selam bebiş")




# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün 

import datetime

tarih = (input("aracınız hangi gün tarihe çıktı 2022/11/9: "))
tarih = tarih.split("/")
trafigeCikis =  datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

simdi = datetime.datetime.now()

fark = simdi - trafigeCikis
days = fark.days



if (days <= 365):
    print("1.servis aralığı")
elif (days > 365) and (days <= 365*2):
    print("2.servis aralığı")
else:
    print("3.servis aralığı")



