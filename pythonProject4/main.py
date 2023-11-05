import math
def cos_taylor(x, n):
    sonuc = 1
    for i in range(1, n):
        if i % 2 == 1:
            k = (-1) ** i * (x ** (2 * i)) / math.factorial(2 * i)
            if k == 0:
                break
            sonuc += k
    return sonuc


PI = 3.14159265358979323846

x = PI / 5

n = int(input("Terim sayisi giriniz: "))


hesaplananDeger = cos_taylor(x, n)

gercekDeger = math.cos(x)

hataPayi = abs(gercekDeger - hesaplananDeger)

print(f"{n} terimli Yaklaşık Değer:", hesaplananDeger)
print("Gerçek Değer:", gercekDeger)
print(f"{n} terimli Kesme Hatası:", hataPayi)
