def Tampilkan_Angka_Ganjil(n):
    for i in range (1, n + 1):
        if i % 2 != 0:
            print(i)

n = int (input("Masukan nilai n: "))
print("Bilangan Ganjil dari :", n, ":")
Tampilkan_Angka_Ganjil(n)
