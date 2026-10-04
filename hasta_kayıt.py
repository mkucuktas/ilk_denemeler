hastalar = []

while True:
    ad = input("Hayvanın adı [bitirmek için boş bırak]: ")
    if ad == "":
        break
    tur = input("Türü: ")
    agirlik = float(input("Ağırlık (kg): "))
    hastalar.append({"ad": ad, "tur": tur, "agirlik": agirlik})

doz_orani = float(input("Doz oranı (mg/kg): "))

for hasta in hastalar:
    doz = hasta["agirlik"] * doz_orani
    print(hasta["ad"], "-", hasta["tur"], "-", hasta["agirlik"], "kg ->", doz, "mg")