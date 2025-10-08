# Soal NIM Ganjil
# Buatlah program Python untuk program Pembelian Tiket Bioskop XX0.

# 1. Validasi Login:
# Gunakan nama sebagai username dan NIM sebagai password.
# Batas percobaan login maksimal 3 kali.
# Jika login gagal 3 kali, program berhenti dan tidak menampilkan menu pembelian tiket.
# Jika login berhasil, program menampilkan menu pembelian tiket.

# 2. Menu Pembelian Tiket
# Tampilan menu pembelian tiket harus terdapat opsi berikut:
# opsi 1 -> Tiket Regular dengan Harga per tiket Rp 50.000
# opsi 2 -> Tiket VIP dengan Harga per tiket Rp.100.000
# opsi 3 -> Tiket VVIP dengan Harga per tiket Rp.150.000
# opsi 4 -> Keluar dari program

# Setelah pengguna memilih opsi tiket, program akan meminta input jumlah tiket yang ingin dibeli.
# Menu akan terus muncul sampai pengguna memilih opsi keluar.

# 3. Tampilan Hasil
# Hitung total bayar dengan menggunakan for (looping sesuai jumlah tiket).
# Tampilkan hasil berupa jenis tiket yang dipilih, jumlah tiket. dan total bayar.

# 4. Rumus
# total bayar = Harga Tiket*Jumlah Tiket.

# 5. POIN PLUS (+)
# Tambahkan ketentuan,
# Jika total bayar >= Rp.300.000, maka ia mendapat potongan 12% dari total bayar akhir.
# Jika total bayar >= Rp.200.000 dan total bayar < Rp.300.000, maka ia mendapat potongan 8% dari total bayar akhir.
# Jika total bayar >= Rp.150.000 dan total bayar < Rp.200.000, maka ia mendapat Poster Film Ekslusif.
# Terapkan error handling sederhana menggunakan if/else tanpa try-except.


Nama = "Sufi Ridho Utomo"
NIM = 2509106101
percobaan = 3
Login_Berhasil = False
Jumlah_Tiket = 0
total = 0
Regular = 50000
VIP = 100000
VVIP = 150000

print(" ")
print("==| Selamat Datang Di Aplikasi XX0 |==")
print("Silahkan Login Terlebih Dahulu!")
print(" ")

while percobaan > 0:
    Nama_Pengguna = input("Masukkan Nama Anda  : ")
    NIM_Pengguna = int(input("Masukkan Password   : "))

    if Nama == Nama_Pengguna and NIM == NIM_Pengguna:
        print(" ")
        print("Login Berhasil! Selamat Datang", Nama)
        Login_Berhasil = True
        break
    else:
        percobaan -= 1
        if percobaan > 0:
            print(" ")
            print("Login Gagal! Silahkan Ulangi Kembali😞")
            print("Batas Limit :", percobaan)
        else:
            print(" ")
            print("Login Anda Mencapai Limit😭!")
            exit()

if Login_Berhasil:
    print("==| Daftar Tiket |== ")
    print("1. Reguler : Rp", Regular)
    print("2. VIP     : Rp", VIP)
    print("3. VVIP    : Rp", VVIP)
    print("4. Keluar")

while True:
    print(" ")
    pilihan = input("Silahkan Masukkan Pilihan Anda : ")
    if pilihan == "4" or pilihan.lower() == "keluar":
        print(" ")
        print("==| Terima Kasih Telah Menggunakan XXO |==")
        exit()
    elif pilihan == "1":
        Tiket_Regular = int(input("Jumlah Tiket Regular : "))
        Jumlah_Tiket  = Tiket_Regular
        Total_Regular   = Regular * Tiket_Regular
        print("Total Harga Tiket Regular Anda :", Total_Regular)
        if Total_Regular >= 300000:
            diskon_12 = int(Total_Regular * 0.12)
            print("Anda Mendapat Diskon 12% : ", diskon_12)
            print("Harga Setelah Diskon :", Total_Regular - diskon_12)
            print(" ")
            print("==| Terima Kasih Telah Menggunakan XXO |==")
        elif 200000 <= Total_Regular < 300000:
            diskon_8 = int(Total_Regular * 0.08)
            print("Anda Mendapat Diskon 8% :", diskon_8)
            print("Harga Setelah Diskon :", Total_Regular - diskon_8)
            print(" ")
            print("==| Terima Kasih Telah Menggunakan XXO |==")
        elif 150000 <= Total_Regular < 200000:
            print("Anda Mendapatkan Bonus Poster Film Eksklusif")
        else:
            print("Anda Tidak Mendapatkan Diskon")
            break
    elif pilihan == "2":
        Tiket_VIP     = int(input("Jumlah Tiket VIP : "))
        Jumlah_Tiket  = Tiket_VIP
        Total_VIP   = VIP * Tiket_VIP
        print("Total Harga Tiket VIP Anda :", Total_VIP)
        if Total_VIP >= 300000:
            diskon_12 = int(Total_VIP * 0.12)
            print("Anda Mendapat Diskon 12% : ", diskon_12)
            print("Harga Setelah Diskon :", Total_VIP - diskon_12)
            print(" ")
            print("==| Terima Kasih Telah Menggunakan XXO |==")
        elif 200000 <= Total_VIP < 300000:
            diskon_8 = int(Total_VIP * 0.08)
            print("Anda Mendapat Diskon 8% :", diskon_8)
            print("Harga Setelah Diskon :", Total_VIP - diskon_8)
            print(" ")
            print("==| Terima Kasih Telah Menggunakan XXO |==")
        elif 150000 <= Total_VIP < 200000:
            print("Anda Mendapatkan Bonus Poster Film Eksklusif")
        else:
            print("Anda Tidak Mendapatkan Diskon")
            break
    elif pilihan == "3":
        Tiket_VVIP    = int(input("Jumlah Tiket VVIP : "))
        Jumlah_Tiket  = Tiket_VVIP
        Total_VVIP   = VVIP * Tiket_VVIP
        print("Total Harga Tiket VVIP Anda :", Total_VVIP)
        if Total_VVIP >= 300000:
            diskon_12 = int(Total_VVIP * 0.12)
            print("Anda Mendapat Diskon 12% : ", diskon_12)
            print("Harga Setelah Diskon :", Total_VVIP - diskon_12)
            print(" ")
            print("==| Terima Kasih Telah Menggunakan XXO |==")
        elif 200000 <= Total_VVIP < 300000:
            diskon_8 = int(Total_VVIP * 0.08)
            print("Anda Mendapat Diskon 8% :", diskon_8)
            print("Harga Setelah Diskon :", Total_VVIP - diskon_8)
            print(" ")
            print("==| Terima Kasih Telah Menggunakan XXO |==")
        elif 150000 <= Total_VVIP < 200000:
            print("Anda Mendapatkan Bonus Poster Film Eksklusif")
        else:
            print("Anda Tidak Mendapatkan Diskon")
            break
    else:
        print(" ")
        print("Upss🤭! Gak Pilihan Lain🙅, Ulang Yahh😉")
        continue