print("==========================================================================")
print("|                       RESTAURANT  \"WARUNG POJOK\"                       |")
print("|        Jl. Bonjer Barat, Sawah Besar, Jakarta Pusat, DKI Jakarta       |")
print("==========================================================================")
print("||                            DAFTAR MAKANAN                            ||")
print("--------------------------------------------------------------------------")
print("||       Kode         |           Menu            |        Harga        ||")
print("--------------------------------------------------------------------------")
print("||        A           |        Nasi  Goreng       |     Rp. 15.000      ||")
print("||        B           |         Mie Goreng        |     Rp. 15.000      ||")
print("||        C           |       Kwetiau Goreng      |     Rp. 15.000      ||")
print("||        D           |          Mie Ayam         |     Rp. 14.000      ||")
print("||        E           |       Ayam  Teriyaki      |     Rp. 12.000      ||")
print("||        F           |         Soto  Ayam        |     Rp. 12.000      ||")
print("==========================================================================")
print("||                            DAFTAR MINUMAN                            ||")
print("--------------------------------------------------------------------------")
print("||       Kode         |           Menu            |        Harga        ||")
print("--------------------------------------------------------------------------")
print("||        G           |        Es Teh Tawar       |     Rp.  3.000      ||")
print("||        H           |        Es Teh Manis       |     Rp.  5.000      ||")
print("||        I           |          Es Jeruk         |     Rp.  7.000      ||")
print("==========================================================================")
print("")

pembeli = input(" Masukkan Nama Pembeli\t: ")
print("")

kode = []
porsi = []
menu = []
harga = []
jumlah = []

i = 0

while True:
  kode.append(input(" Masukkan Kode Menu\t: "))
  porsi.append(int(input(" Jumlah Porsi\t\t: ")))

  if kode[i] == "A" or kode[i] == "a":
    menu.append("Nasi  Goreng")
    harga.append("Rp. 15.000")
    jumlah.append(porsi[i]*15000)
  elif kode[i] == "B" or kode[i] == "b":
    menu.append("Mie Goreng")
    harga.append("Rp. 15.000")
    jumlah.append(porsi[i]*15000)
  elif kode[i] == "C" or kode[i] == "c":
    menu.append("Kwetiau Goreng")
    harga.append("Rp. 15.000")
    jumlah.append(porsi[i]*15000)
  elif kode[i] == "D" or kode[i] == "d":
    menu.append("Mie Ayam")
    harga.append("Rp. 14.000")
    jumlah.append(porsi[i]*14000)
  elif kode[i] == "E" or kode[i] == "e":
    menu.append("Ayam  Teriyaki")
    harga.append("Rp. 12.000")
    jumlah.append(porsi[i]*12000)
  elif kode[i] == "F" or kode[i] == "f":
    menu.append("Soto  Ayam")
    harga.append("Rp. 12.000")
    jumlah.append(porsi[i]*12000)
  elif kode[i] == "G" or kode[i] == "g":
    menu.append("Es Teh Tawar")
    harga.append("Rp.  3.000")
    jumlah.append(porsi[i]*3000)
  elif kode[i] == "H" or kode[i] == "h":
    menu.append("Es Teh Manis")
    harga.append("Rp.  5.000")
    jumlah.append(porsi[i]*5000)
  elif kode[i] == "I" or kode[i] == "i":
    menu.append("Es Jeruk")
    harga.append("Rp.  7.000")
    jumlah.append(porsi[i]*7000)
  else:
    print("Kode Salah")
  
  lanjut = input(" Lanjut Memesan (Y/T)\t: ")
  print("")
  if lanjut == "T" or lanjut == "t":
    break
  else:
    i+=1

print("==========================================================================")
print("|                       RESTAURANT \"WARUNG POJOK\"                        |")
print("|        Jl. Bonjer Barat, Sawah Besar, Jakarta Pusat, DKI Jakarta       |")
print("==========================================================================")
print("|| {:<69}||".format("Nama Pembeli : " + pembeli))
print("==========================================================================")
print("||   Kode   |         Menu         |   Banyak   |      Total Harga      ||")
print("--------------------------------------------------------------------------")

total = 0
a = 0

while a <= i:
  total+=jumlah[a]
  print("||{:^10}|{:^22}|{:^12}|{:^23}||".format(kode[a].upper(), menu[a], porsi[a], "Rp. " + str(jumlah[a])))
  a+=1

print("==========================================================================")
print("")

pajak = total * 0.1
totalbayar = total + pajak
print(" Jumlah Bayar\t\t: Rp.", total)
print(" Pajak 10%\t\t: Rp.", int(pajak))

if totalbayar > 100000:
  diskon = totalbayar * 0.05
  disbul = round(diskon, -2)
  totalbayar-=disbul
  print(" Diskon 5%\t\t: Rp.", int(disbul))

print(" Total Bayar\t\t: Rp.", int(totalbayar))

uang = 0

while uang < totalbayar:
  
  uang = int(input(" Masukkan Uang Anda\t: Rp. "))
  kembali = uang - totalbayar
  
  if uang < totalbayar:
    print("")
    print("                     !! Maaf, Uang Anda Kurang !!                     ")
    print("              !! Silahkan Masukkan Uang Anda Kembali !!               ")
    print("")
    continue
  else:
    print(" Kembalian Anda\t\t: Rp.", int(kembali))

print("")
print("---------------------------- Terima Kasih --------------------------------")