#Looping kondisi batas 

n = int(input("jumlah 1 sampai n, n="))
total = 0
i = 1

while i <= n:
    total = total + i
    i = i + i
    #0 + 1 = 1 + 2 = 3 + 3 = 6
    print ("jumlah :",total)