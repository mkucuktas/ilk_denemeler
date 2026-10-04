# Birden fazla hayvan için toplu doz hesabı (sadece öğrenme amaçlı)

doz_orani = float(input("Doz oranı (mg/kg): "))

agirliklar = [4.5, 12, 30, 8.2, 21, 30]

for agirlik in agirliklar:
    doz = agirlik * doz_orani
    print(agirlik, "kg ->", doz, "mg")