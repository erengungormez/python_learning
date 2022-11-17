# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
# sayı = int(input('Sayı: '))
# result = (sayı > 50) and (sayı < 100)

# print(f"Girdiğiniz sayı 100 ve 50 arasında : {result}")


# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.

# sayı = int(input("sayı : "))

# result = ( sayı > 0) and (sayı % 2 == 1)

# print(f"Girdiğiniz sayı pozitif ve tek sayı olma değeri : {result}")

# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
# username = "erewn"
# password = 123123123

# result = input("username : ")
# result2 = int(input("password : "))

# sonuc = (username == result) and (password == result2)

# print(f"Kullanıcı adınız ve şifreniz : {sonuc}")




# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

# a = int(input("a : "))  
# b = int(input("b : "))
# c = int(input("c : "))

# result = (a > b) and (a > c)
# print(f"a en büyük sayıdır : {result}")

# result = (b > a) and (b > c)
# print(f"b en büyük sayıdır : {result}")

# result = (c > a) and (c > b)
# print(f"c en büyük sayıdır : {result}")




# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti yoksa kaldı yazdırınız
# a-) Ortalama 50 bile olsa final notu  en az 50 olmalıdır,
# b-) ^Finalden 70 alıdığında ortlamanın önemi olmasın. 

# vize1 = float(input("vize notu : "))
# vize2 = float(input("vize notu : "))
# final = float(input("final notu : "))

# sonuc = ((vize1 + vize2)/2)*0.6 + (final * 0.4)
# result = (sonuc >= 50)  and (final >= 50)
# print(f"öğreninin ortlaması {sonuc} ve sınıfı geçme durumu: {result}")




# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)


isim = input("isim : ")
kilo = float(input("kilo : "))
boy = float(input("boy : "))

indeks = (boy ** 2)/ kilo

zayıf = (indeks >= 0) and (indeks <= 18.4)
normal = (indeks >= 18.5) and (indeks <= 24.9)
fazlakilolu = (indeks >= 25) and (indeks <= 29.9)
obez = (indeks >= 30) and (indeks <= 35)



print(f"{isim} kilo indeksin :{indeks} ve kilo değerlendirmen  zayıf {zayıf}")
print(f"{isim} kilo indeksin :{indeks} ve kilo değerlendirmen  normal {normal}")
print(f"{isim} kilo indeksin :{indeks} ve kilo değerlendirmen  fazla kilolu {fazlakilolu}")
print(f"{isim} kilo indeksin :{indeks} ve kilo değerlendirmen  obez {obez}")

