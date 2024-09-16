# 1. Seviye: Basit
def toplama_islemi():
    # Kullanıcıdan iki sayı alıyoruz.
    sayi1 = float(input("Birinci sayıyı girin: "))
    sayi2 = float(input("İkinci sayıyı girin: "))

    # Sayıları topluyoruz ve toplam değişkenine atıyoruz.
    toplam = sayi1 + sayi2

    # Sonucu ekrana yazdırıyoruz
    print("Sayıların toplamı:", toplam)


# 2. Seviye: Orta
def sayilari_topla():
    # 1'den 100'e kadar olan sayıları toplamak için değişken tanımlıyoruz
    toplam = 0

    # 1'den 100'e kadar sayıları for döngüsü kullanarak topluyoruz.
    for sayi in range(1, 101):
        toplam += sayi

    # Sonucu ekrana yazdırıyoruz.
    print("1'den 100'e kadar olan sayıların toplamı:", toplam)


# 3. Seviye: İleri
def asal_kontrol():
    # Asal sayıyı kontrol eden bir fonksiyon tanımlıyoruz.
    def asal_mi(sayi):
        if sayi < 2:
            return False
        for i in range(2, int(sayi**0.5) + 1):
            if sayi % i == 0:
                return False
        return True

    # Kullanıcıdan sayı alıyoruz
    sayi = int(input("Bir sayı girin: "))

    # Asal olup olmadığını kontrol edip sonucu ekrana yazdırıyoruz.
    if asal_mi(sayi):
        print(sayi, "asal bir sayıdır.")
    else:
        print(sayi, "asal bir sayı değildir.")


# 4. Seviye: Zor
def dizi_tekrar_kontrol():
    # Dizi içindeki elemanların tekrar edip etmediğini kontrol eden fonksiyon
    def tekrar_var_mi(dizi):
        eleman_seti = set()
        for eleman in dizi:
            if eleman in eleman_seti:
                return True
            eleman_seti.add(eleman)
        return False

    # Kullanıcıdan dizi elemanlarını alıyoruz ve split fonksiyonu ile sayıları ayırıp diziye tanımlıyoruz.
    dizi = input("Dizi elemanlarını boşluklarla ayırarak girin: ").split()

    # Tekrar eden eleman olup olmadığını kontrol edip sonucu ekrana yazdırıyoruz.
    if tekrar_var_mi(dizi):
        print("Dizide tekrar eden elemanlar var.")
    else:
        print("Dizide tekrar eden eleman yok.")


# Menü yapısı
def menu():
    while True:
        print("\n---- Menü ----")
        print("1. İki sayıyı topla (Seviye: Basit)")
        print("2. 1'den 100'e kadar sayıları topla (Seviye: Orta)")
        print("3. Asal sayı kontrolü yap (Seviye: İleri)")
        print("4. Dizi elemanlarının tekrar edip etmediğini kontrol et (Seviye: Zor)")
        print("5. Çıkış")

        # Kullanıcıdan seçim alıyoruz
        secim = input("Bir seçenek girin (1-5): ")

        # Seçime göre ilgili fonksiyonu çalıştırıyoruz
        if secim == "1":
            toplama_islemi()
        elif secim == "2":
            sayilari_topla()
        elif secim == "3":
            asal_kontrol()
        elif secim == "4":
            dizi_tekrar_kontrol()
        elif secim == "5":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


# Menü fonksiyonunu başlatıyoruz
menu()
