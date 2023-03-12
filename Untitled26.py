#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

print("Merhaba! Benim adım Kaan. Seninle bir oyun oynayacağız.")
print("Ben bir sayı tutacağım ve sen bunu tahmin etmeye çalışacaksın.")
print("Hazır mısın? Haydi başlayalım!")

# Rastgele bir sayı seçin (1-20 arasında)
sayi = random.randint(1, 20)
tahmin_hakki = 5

while tahmin_hakki > 0:
    print("Kalan tahmin hakkın:", tahmin_hakki)
    tahmin = int(input("Tahminin nedir? "))

    if tahmin < sayi:
        print("Daha büyük bir sayı tahmin etmelisin.")
    elif tahmin > sayi:
        print("Daha küçük bir sayı tahmin etmelisin.")
    else:
        break

    tahmin_hakki -= 1

if tahmin == sayi:
    print("Tebrikler! Doğru tahmin ettin!")
else:
    print("Maalesef, doğru sayıyı tahmin edemedin. Sayım", sayi, "idi.")

print("Oyun bitti. Tekrar oynamak ister misin?")


# In[ ]:




