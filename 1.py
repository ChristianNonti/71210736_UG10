print("\(^o^ selamat datang di kalkulator sederhana (^o^)/")
print("ketik 1 untuk penjumlahan ")
print('ketik 2 untuk penguranan ')
print('ketik 3 untuk perkalian ')
print('ketik 4 untuk pembagian ')
print("ketik 5 untuk menghitung modulus.")
print("ketik 6 untuk menghitung pemangkatan")

pilihan = input("Masukkan pilhan anda :")


pilihan1 = input("Masukan bilangan pertama :")
pillhan2 = input("Masukan bilangan kedua :")


if pilihan == '1':
    hasil = pilihan1 + pillhan2
    print(f'Hasil dari {pilihan1} di jumlahkan dengan + {pillhan2} adalah = {hasil}')
elif pilihan == '2':
    hasil = pilihan1 - pillhan2
    print(f'Hasil dari{pilihan1}  di kurangkan dengan  {pillhan2} adalah = {hasil}')
elif pilihan == '3':
    hasil = pilihan1 * pillhan2
    print(f'Hasil dari{pilihan1} di kalikan dengan {pillhan2} adalah = {hasil}')
elif pilihan == '4':
    hasil = pilihan1 / pillhan2
    print(f'Hasil  dari {pilihan1} di bagikan dengan {pillhan2}  adalah = {hasil}')
elif pilihan == '5':
    hasil = pilihan1 % pillhan2
    print(f'Hasil dari {pilihan1} di modulus dengan  {pillhan2} adalah = {hasil}')
elif pilihan == '6':
    hasil = pilihan1 ** pillhan2
    print(f'Hasil dari {pilihan1} di pangkatkan dengan {pillhan2} adalah = {hasil}')

else:
  print('Tidak valid')

