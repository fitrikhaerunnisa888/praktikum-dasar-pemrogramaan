print("Langkah 1")
for angka in range(1, 11):
    if angka % 2 == 0:
        continue
    print(angka, end=" ")
print()

print("\nLangkah 2")
for angka in range(1, 100):
    if angka % 7 == 0 and angka % 5 == 0:
        print(f"Bilangan pertama yang habis dibagi 7 dan 5 adalah {angka}")
        break

print("\nLangkah 3")
for angka in range(1, 201):
    if angka % 4 == 0 and angka % 6 == 0:
        print(f"Bilangan pertama yang habis dibagi 4 dan 6 adalah {angka}")
        break


print("\nSegitiga terbalik")
for baris in range(1, 6):
    for kolom in range(6 - baris):
        print("*", end=" ")
    print()