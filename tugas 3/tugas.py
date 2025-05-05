import math
import json

def hitung(angka1, angka2, operasi):
    """Melakukan operasi matematika."""
    if operasi == "+":
        return angka1 + angka2
    elif operasi == "*":
        return angka1 * angka2
    else:
        return "Operasi tidak valid"

def simpan_hasil(hasil):
    """Menyimpan hasil perhitungan ke file JSON."""
    data = {"hasil": hasil}
    with open("hasil.json", "w") as file:
        json.dump(data, file)
    print("Hasil disimpan ke hasil.json")

# Program utama
while True:
    print("\n=== Kalkulator Sederhana ===")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Keluar")

    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == "1":
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = hitung(angka1, angka2, "+")
        print("Hasil:", hasil)
        simpan_hasil(hasil)
    elif pilihan == "2":
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
        hasil = hitung(angka1, angka2, "*")
        print("Hasil:", hasil)
        simpan_hasil(hasil)
    elif pilihan == "3":
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid.")