
hak = 0
devam = "e"

x = 352

# result = 5 < x < 10

# and

result = (5 < x) and (x < 10)  # True, True => True   ( Her iki koşul da sağlanmalı) 

result = (hak > 0) and (devam == "e")

# or

result = (x > 0) or (x % 2 == 0 ) # True , False => True  (Bir koşulun sağlaması yeterli)
                                 

# not

result = not( x > 0) # tam tersini almaya yarar

# x, 5 ile 10 arasında olan bir çift sayı mı?

result = ((x > 5) and (x < 10)) and (x % 2 == 0) 


print(result)