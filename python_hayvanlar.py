hayvanlar = ["Pamuk", "Karabaş", "Tekir", "Zeytin"]

print(hayvanlar)
print(hayvanlar[0])
print(hayvanlar[2])
print(len(hayvanlar))

hayvanlar.append("Boncuk")
print(hayvanlar)

print()
print("Bugünkü hastalar:")

for hayvan in hayvanlar:
    print("-", hayvan)