import json

# Önceki kayıtları dosyadan oku (dosya yoksa boş liste ile başla)
try:
    with open("hastalar.json", "r", encoding="utf-8") as dosya:
        hastalar = json.load(dosya)
except FileNotFoundError:
    hastalar = []

print("Kayıtlı hasta sayısı:", len(hastalar))

# Yeni hayvanları ekle
while True:
    ad = input("Hayvanın adı (bitirmek için sadece Enter'a bas): ")
    if ad == "":
        break
    tur = input("Türü: ")
    agirlik = float(input("Ağırlık (kg): "))
    hastalar.append({"ad": ad, "tur": tur, "agirlik": agirlik})

    # Her eklemeden sonra hemen dosyaya yaz
    with open("hastalar.json", "w", encoding="utf-8") as dosya:
        json.dump(hastalar, dosya, ensure_ascii=False, indent=2)
    print("Kaydedildi. Toplam hasta:", len(hastalar))

# Doz hesabı
doz_orani = float(input("Doz oranı (mg/kg): "))

for hasta in hastalar:
    doz = hasta["agirlik"] * doz_orani
    print(hasta["ad"], "-", hasta["tur"], "-", hasta["agirlik"], "kg ->", doz, "mg")