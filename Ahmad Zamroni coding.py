print('_________________Program Konversi Suhu________________')
print('Ahmad Zamroni, NIM 210441100158')
print('______________________________________________________')

print("Selamat Datang Di Konversi Suhu. Pilih Satuan Temperatur Yang Ingin Anda Konversikan ")
print('===============')
print('1.   Celcius   ')
print('2.  Fahrenheit ')
print('3.    Kelvin   ')
print('4.    Reamur   ')
print('===============')
def main():
 try:
    print('--------------')
    inputMenu = int(input('Masukan pilihan menu : '))
    if inputMenu == 1:
        c = float(input("Masukan Suhu Celcius Yang Ingin Di Konversikan : "))
        f = ((9 / 5 * c) + 32)
        k = (c + 273)
        r = (4 / 5 * c)
        print('Hasil Celcius = ', + c)
        print('Hasil Fahrenheit = ','{:.1f}'.format(f))
        print('Hasil Kelvin = ','{:.1f}'.format(k))
        print('Hasil Reamur = ','{:.1f}'.format(r))

    if inputMenu == 2:
        f = float(input("Masukan Suhu Fahrenheit Yang Ingin Di Konversikan : "))
        c = (5 / 9 * (f - 32))
        k = ((5 / 9 * (f - 32)) + 273)
        r = (4 / 9 * (f - 32))
        print('Hasil Fahrenheit = ', + f)
        print('Hasil Celcius = ', '{:.1f}'.format(c))
        print('Hasil Kelvin = ', '{:.1f}'.format(k))
        print('Hasil Reamur = ', '{:.1f}'.format(r))

    if inputMenu == 3:
        k = float(input("Masukan Suhu Kelvin Yang Ingin Di Konversikan : "))
        c = (k - 273)
        f = ((9 / 5) * (k - 273) + 32)
        r = (4 / 5 * (k - 273))
        print('Hasil Kelvin = ', + k)
        print('Hasil Celcius = ', '{:.1f}'.format(c))
        print('Hasil Fahrenheit = ', '{:.1f}'.format(f))
        print('Hasil Reamur = ', '{:.1f}'.format(r))
        print('Terimakasih Sudah Menggunakan Alat Konversi Ini')

    if inputMenu == 4:
        r = float(input("Masukan Suhu Reamur Yang Ingin Di Konversikan : "))
        c = (5 / 4 * r)
        f = ((9 / 4 * r) + 32)
        k = (5 / 4 * r + 273)
        print('Hasil Reamur = ', + r)
        print('Hasil Celcius = ', '{:.1f}'.format(c))
        print('Hasil Fahrenheit = ', '{:.1f}'.format(f))
        print('Hasil Kelvin = ', '{:.1f}'.format(k))
        print('Terimakasih Sudah Menggunakan Alat Konversi Ini')

 except:
    print("Masukkan Bil Valid !!!")

i=0
while i == 0:
    main()
