"""
1-100 arasında rasgele üretilecek bir sayıyı aşağı yukarı ifadelerle bulmaya çalışın (hak=5)

** "random modülü" için "pyhton random" şeklşnde arama yapın
** 100 üzerinen puanlama yapın. Her soru 20 puan 
*** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayııs üzerinden hesaplanısn

"""


import random

sayi = random.randint(1,10)
can = int(input("kaç hak istersiniz: "))
hak = can
sayac = 0

while hak>0:
    hak-=1
    sayac+=1
    tahmin= int(input("tahmin: "))

    if sayi == tahmin:
        print(f"tebrikler {sayac}.defada doğru bildiniz.Toplam puanınız {100-(100/can)*(sayac-1)}")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşşağı")

    if hak == 0:
        print(f"hakkınız bitti. tutulan sayı {sayi}")



