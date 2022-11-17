# sayilar = [4,6,9,10,35,57,89,125,244]

# # 1: sayilar listesini while ile ekrana yazdırın.
# i  = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1


# # 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# # ekrana yazdırın.
# baslangic = int(input("başlangıç değeri : "))
# bitis = int(input("bitiş değeri : "))

# i = baslangic

# while i < bitis:
#     i += 1
# #     if (i % 2 == 1):
# #         print(i)

# # 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.

# number = 100

# while number > 0:
#     number -= 1
#     print(number)

# # 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

# numbers = []

# i = 0

# while i < 5 :
#     sayi = int(input("sayı: "))
#     numbers.append(sayi)
#     i += 1
    
# numbers.sort()
# print(numbers)    

# 5: Kullanıcıdan alacağınız sınırsız ürün bilsiinin  urunler listesi içinde saklayınız 
#  *** ürün sayısını kullanıcıya sorun
#  *** dictionary listesi (name,price) şeklinde olsun
#  *** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin

urunler = []

adet = int(input("kaç adet ürün almak istiyorsunuz? : "))

i = 0

while (i<adet):
    name = input("ürün ismi: ")
    price = input("ürün fiyat: ")
    urunler.append({
        'name': name,
        'price': price
    })
    i += 1

for urun in urunler:
    print(f"urun adı {urun['name']} ürün fiyatı {urun['price']}")











