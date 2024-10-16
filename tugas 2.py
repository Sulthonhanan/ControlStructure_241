def Cari_Terbesar (a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
a = int (input("Masukan Angka Pertama:"))
b = int (input("Masukan Angka Kedua:"))
c = int (input("Masukan Angka Ketiga:"))
Angka_Terbesar = Cari_Terbesar (a,b,c)
print ("Angka yang memiliki nilai terbesar adalah:", Cari_Terbesar (a,b,c))

