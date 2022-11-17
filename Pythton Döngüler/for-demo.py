# sayilar= [1,3,5,7,9,12,19,21]

# 1 - Sayilar listesindeki hangi sayılar 3 ün katıdır ?

# for n in sayilar:
#     uk = n % 3
#     if 0 == uk:
#         print("sayınız 3 ün katı")
#     else:
#         print("3 ün katı değil değil")

# # 2 - Sayilar listesimdeki sayıların toplamı kaçtır?
# toplam = 0
# for number in sayilar:
#     toplam += number
# print("toplam : ",toplam)

# 3 - Sayilar listesindeki tek sayıların karesini alınız.

# for sayi in sayilar:
#     if (sayi % 3 == 0):
#         print(sayi ** 2)

# sehirler =  ["kocaeli","istanbul","ankara","izmir","bursa"]

# # 4 - Şehirlerden hangileri en az 5 karakterlidir?

# for sehir in sehirler:
#         if (len(sehir) <= 5):
#             print(sehir)

urunler = [
    {"name" : "samsung S6" , "price" : "3000"},
    {"name" : "samsung S7" , "price" : "4000"},
    {"name" : "samsung S8" , "price" : "5000"},
    {"name" : "samsung S9" , "price" : "6000"},
    {"name" : "samsung S10" , "price" : "7000"},

]

# 5 - Ürünlerin fiyatlaarı tıplamın nedir?
toplam = 0
for urun in urunler:
    fiyat = int(urun["price"])
    toplam += fiyat
print(toplam)


# 5 - Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz

for urun in urunler:
    if (int(urun["price"]) <= 5000):
        print(urun["name"])