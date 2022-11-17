# list = [1,2,3]

# for item in list:          #1 den 3 e kadar olan sayıları yazdırmaya yazdırdık
#     print(item)



# for item in range(10):       # liste belirlemeden 'range' metodula 0 dan 10 a kadar yazdırmaya yaradı
#     print(item)


# for item in range(10,100): # 10 dan başla 100 e kadar git
#     print(item)


# for item in range(10,100,5): # 10 dan başla 5 er şekilfde 100 e kadar git
#     print(item),

# for item in range(50,100,20):
#     print(list(range(50,100,20)))




                                    # enumerate

# index = 0
# greeting = "Hello"

# for letter in greeting:
#     print(f"letter: {letter} index: {index}")
#     index+=1


# greeting = "Hello"

# for letter,index in enumerate(greeting):
#     print(f"letter: {letter} index: {index}")

                                    # zip    listeleri birleştirmek için kullanılıyor


list1 = [1,2,3]
list2 = ["a","b","c"]
list3 = [100,200,300]

# print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a)
