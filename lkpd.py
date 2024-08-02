#No 3
print ("======= Soal 3 =======")

j = int(input("Inputkan jam : "))
m = int(input("Inputkan menit : "))
d = int(input("Inputkan detik : "))

def konversiDetik(j,m,d):
    j = j * 3600
    m = m * 60
    return (j + m + d)
hasil = konversiDetik(j,m,d)

print ("Nilai Detik", hasil)

print ("=======================")

#No 4
print ("======= Soal 4 =======")

def konversiJMD(total_d):
    j = total_d // 3600
    sisa_d = total_d % 3600
    m = sisa_d // 60
    d = sisa_d % 60
    
    return j, m, d

total_d = int(input("Masukkan total detik: "))

j, m, d = konversiJMD(total_d)

print(f"{j} jam {m} menit {d} detik")

print ("=======================")

#No 5
print ("======= Soal 5 =======")

i = 0

while i <= 50:
    print (i)
    i += 1

print ("=======================")

