#1.Adding Two Numbers

# Memasukkan Inputan Angka
angka1 = input('Tulis angka pertama: ')
angka2 = input('Tulis angka kedua: ')

# Mengkonversi Angka lalu Menjumlahkannya
sum = int(angka1) + int(angka2)

# Menampilkan Hasil Penjumlahan
print('Hasil Penjumlahan {0} dan {1} adalah {2}'.format(angka1, angka2, sum))


#2.Calculating Square Roots

# Memasukkan Inputan Angka
angka = float(input('Tuliskan Angka: '))

# Menghitung Akar Kuadrat
akar_kuadrat = angka ** 0.5

#Menampilkan Hasil Akar Kuadrat
print('Akar Kuadrat dari %0.3f adalah %0.3f'%(angka ,akar_kuadrat))


#3.Calculating the Area of ​​a Triangle

# Menginput Alas dan Tinggi Segitiga
alas = float(input('Tulis Alas Segitiga: '))
tinggi = float(input('Tulis Tinggi Segitiga: '))

# Hitung Luas Segitiga
luas = (alas * tinggi) / 2

#Menampilkan Hasil Perhitungan
print('Luas Segitiga adalah %0.2f' %luas)


#4.Calculating the Volume of a Cube

# Menginput Sisi Kubus
sisi = float(input('Tulis Sisi Kubus: '))

# Hitung Volume Kubus
volume = sisi ** 3

#Menampilkan Hasil Perhitungan
print('Volume Kubus adalah %0.2f' %volume)


#5.Solving Quadratic Equations

# Menyelesaikan Persamaan Kuadrat ax**2 + bx + c = 0

# Mengimpor Modul Cmath
import cmath

# Menginput Angka
a = int(input('Tulis a: '))
b = int(input('Tulis b: '))
c = int(input('Tulis c: '))

# Menghitung Diskriminan
d = (b**2) - (4*a*c)

# Menghitung x1 dan x2
x1 = (-b-cmath.sqrt(d))/(2*a)
x2 = (-b+cmath.sqrt(d))/(2*a)

#Menampilkan Hasil x1 dan x2
print('Hasil Persamaan Kuadrat adalah {0} dan {1}'.format(x1,x2))


#7.Swapping Variable Values

# Menginput Nilai Variabel
x = input('Tuliskan nilai x: ')
y = input('Tuliskan nilai y: ')

# Membuat Variabel tukar dan Menukar nilai Variabel lain
tukar = x
x = y
y = tukar

#Menampilkan Nilai Variabel Setelah Ditukar
print('Nilai x Setelah Ditukar adalah: {}'.format(x))
print('Nilai y Setelah Ditukar adalah: {}'.format(y))

#8.Generate Random Numbers

# Menampilkan Angka Acak antara 0 sampai 20

# Mengimpor Modul Random
import random

#Menampilkan Angka Acak
print(random.randint(0,20))

#9.Convert Kilometers to Miles

# Menginput Jarak dalam Satuan Kilometer
kilometer = float(input("Tuliskan Jarak dalam Kilometer: "))

# Nilai Faktor Konversi
faktor_konversi = 0.621371

# Menghitung Jarak dalam Satuan Mil
mil = kilometer * faktor_konversi

# Menampilkan Hasil Konversi Jarak
print('%0.2f Kilometer sama dengan %0.2f Mil' %(kilometer,mil))

#10.Change Celsius to Fahrenheit

# Menginput Suhu dalam Derajat Celcius
celcius = float(input("Tuliskan Suhu dalam Celcius: "))

# Menghitung Suhu dalam Derajat Fahrenheit
fahrenheit = (celcius * 1.8) + 32

#Menampilkan Hasil Konversi Jarak
print('%0.2f Derajat Celcius sama dengan %0.2f Derajat Fahrenheit' %(celcius,fahrenheit))