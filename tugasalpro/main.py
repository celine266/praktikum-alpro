# Meminta input dari pengguna
target_saldo = int(input("Target saldo: "))
saldo_awal = int(input("Saldo awal: "))
setoran = int(input("Besar setoran tiap kali menabung: "))

# Cek ketentuan nomor 5: jika saldo awal sudah mencapai atau melebihi target
if saldo_awal >= target_saldo:
    print("Target sudah tercapai, tidak perlu menabung.")
else:
    saldo_saat_ini = saldo_awal
    jumlah_menabung = 0
    
    # Ketentuan nomor 1: menggunakan perulangan while
    while saldo_saat_ini < target_saldo:
        jumlah_menabung += 1
        
        # Ketentuan nomor 2: saldo bertambah sebesar setoran
        saldo_saat_ini += setoran
        
        # Ketentuan nomor 3: bonus Rp10.000 untuk kelipatan 4
        keterangan_bonus = ""
        if jumlah_menabung % 4 == 0:
            saldo_saat_ini += 10000
            keterangan_bonus = " (bonus)"
            
        # Menampilkan nomor penabungan dan saldo saat itu
        print(f"Menabung ke-{jumlah_menabung}: Rp{saldo_saat_ini}{keterangan_bonus}")
        
    # Ketentuan nomor 4: menampilkan total penabungan dan saldo akhir
    print(f"Target tercapai setelah {jumlah_menabung} kali menabung Saldo akhir: {saldo_saat_ini}")
