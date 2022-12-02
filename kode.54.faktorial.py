# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
n = int(input("Masukan Nilai n : "))

# Mengkonversi ada 3 cara
#1 looping for
faktorial1 = 1

for i in range(1, n + 1):
  faktorial1 *= i

#2 looping rekursif
def hitung_faktorial (n):
    if n > 2:
     return n * hitung_faktorial(n - 1)

    return 2
faktorial2 = hitung_faktorial(n)

#3 Fungsi Math.factorial()
import math
faktorial3 = math.factorial(n)

# Menampilkan Hasil
print('==========================================================')
print('Maka Nilai Faktorial1 ',n,' =',faktorial1)
print('Maka Nilai Faktorial2 ',n,' =',faktorial2)
print('Maka Nilai Faktorial3 ',n,' =',faktorial3)
print('==========================================================')
