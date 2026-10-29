#Latihan Looping Pengelompokan Masalah 

suhu_tertinggi = None
urutan_tertinggi =  0 
count_lebih_80 = 0
total_suhu_80 = 0
count_suhu_80 = 0

for i in range(1,9) :
    suhu = int(input(f"Suhu pencatatan ke- {1}"))

    #Pola Nilai Ekstrem 
    if suhu_tertinggi is None or suhu > suhu_tertinggi:
        suhu_tertinggi = suhu
        urutan_tertinggi = i 

        #Pola penyaringan + pencacah + Akumulator 
        if suhu > 80 :
            count_lebih_80 += 1
            total_suhu_80 += 1
            count_suhu_80 += 1

            print(f"Suhu tertinggi: {suhu_tertinggi } (pencatatan ke={urutan_tertinggi})")

            if count_lebih_80 == 0 :
                print("Tidak ada suhu yang melebihi 80")
            else :
                print(f"Suhu melebihi 80 : {count_lebih_80} kali")
                print