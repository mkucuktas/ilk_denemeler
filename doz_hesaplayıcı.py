# Doz hesaplayıcı (birden fazla hayvan için)

while True:
    agirlik = float(input("Hayvanın ağırlığı (kg) [çıkmak için 0 yaz]: "))

    if agirlik == 0:
        print("Program kapatılıyor.")
        break

    if agirlik < 0:
        print("Hata: Ağırlık negatif olamaz.")
        continue

    doz_orani = float(input("Doz oranı (mg/kg): "))
    toplam_doz = agirlik * doz_orani
    print("Toplam doz:", toplam_doz, "mg")
    print()

	