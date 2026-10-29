#studi_kasus.py
jumlah = int(input("Masukkan jumlah mahasiswa: "))

nilai_mahasiswa = []
jumlah_lulus = 0
jumlah_remedial = 0
jumlah_tidak_lulus = 0

for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)

    # Memastikan nilai berada pada rentang 0-100
    while True:
        nilai = int(input("Masukkan nilai kuis (0-100): "))

        if nilai >= 0 and nilai <= 100:
            break
        else:
            print("Nilai tidak valid! Masukkan nilai 0-100.")

    nilai_mahasiswa.append(nilai)

    # Mengelompokkan nilai dengan percabangan
    if nilai >= 85:
        kategori = "Lulus Sangat Baik"
        jumlah_lulus += 1
    elif nilai >= 60:
        kategori = "Lulus"
        jumlah_lulus += 1
    elif nilai >= 40:
        kategori = "Remedial"
        jumlah_remedial += 1
    else:
        kategori = "Tidak Lulus"
        jumlah_tidak_lulus += 1

    print("Nilai:", nilai)
    print("Kategori:", kategori)

# Menghitung rekap akhir
rata_rata = sum(nilai_mahasiswa) / jumlah
nilai_tertinggi = max(nilai_mahasiswa)

print("\n===== REKAP NILAI KELAS =====")
print("Jumlah mahasiswa:", jumlah)
print("Rata-rata nilai:", round(rata_rata, 2))
print("Nilai tertinggi:", nilai_tertinggi)
print("Jumlah lulus:", jumlah_lulus)
print("Jumlah remedial:", jumlah_remedial)
print("Jumlah tidak lulus:", jumlah_tidak_lulus)