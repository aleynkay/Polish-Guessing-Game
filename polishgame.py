import random
import time

tutulan_sayi = random.randint(1, 100)

tahmin = None
tahmin_sayisi = 0

print("oyun mod 1 == sayi tutan bilgisayar")
print("oyun mod 2 == tahmin eden bilgisayar")
print()

oyunmod = int(input("Lütfen oyun modu seç(1 ya da 2) :"))
if oyunmod == 1:
    while tahmin != tutulan_sayi:
        tahmin = int(input("1 ile 100 arasinda bir sayi tahmin edin: "))
        tahmin_sayisi += 1 
        if tahmin < tutulan_sayi:
            print("Daha büyük bir sayi girin.")
        elif tahmin > tutulan_sayi:
            print("Daha küçük bir sayi girin.")
        else:
            print(f"Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettiniz. Tutulan sayi: {tutulan_sayi}")

if oyunmod == 2:
    print("1 ile 100 arasinda bir sayi tutun ve aklinizda tutun.")
    print()
    print("Bilgisayarin bu sayiyi tahmin etmesine yardimci olun.")
    print()
    
    lower_bound = 1
    upper_bound = 100
    tahmin_sayisi = 0
    dogru_tahmin = False

    while not dogru_tahmin:
        print("bilgisayar tahmin ediyor......")
        time.sleep(2)
        tahmin = random.randint(lower_bound, upper_bound)
        tahmin_sayisi += 1
        print(f"Bilgisayarin tahmini: {tahmin}")
        kullanici_geri_bildirim = input("Eğer tahmin doğruysa 'd', daha büyükse 'b', daha küçükse 'k' girin: ").lower()
        
        if kullanici_geri_bildirim == 'd':
            dogru_tahmin = True
            print(f"Tebrikler! Bilgisayar {tahmin_sayisi} denemede doğru tahmin etti. Tutulan sayi: {tahmin}")
        elif kullanici_geri_bildirim == 'b':
            lower_bound = tahmin + 1
        elif kullanici_geri_bildirim == 'k':
            upper_bound = tahmin - 1
        else:
            print("Geçersiz giriş. Lütfen 'd', 'b' veya 'k' girin.")