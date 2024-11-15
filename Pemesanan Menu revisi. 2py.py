Menu_Makanan = ["Ayam Goreng", "Ayam Bakar", "Ayam Gulai", "Ayam Pop", "Dendeng Balado", "Gulai Tunjang", "Gulai Kepala Ikan", "Perkedel Kentang", "Telur Dadar"]
Menu_Minuman = ["Es Teh Manis", "Es Teh Tawar", "Kopi Hitam", "Kopi Susu", "Es Jeruk", "Es Tebu", "Jus Alpukat", "Jus Jeruk", "Jus Mangga"]
Tambahan = ["Daun Singkong", "Sambal Merah", "Sambal Hijau", "Serundeng", "Kuah Rendang"]
Harga_Makanan = [8000, 8000, 12000, 15000, 20000, 15000,25000,5000, 5000,8000]
Harga_Minuman = [2500, 2500, 3000, 5000, 8000, 10000, 12000, 10000, 12000]
Harga_Tambahan = [1500, 2000, 2000, 2000, 2500]
pesan = True
jumlah_pemesanan_makanan = [0] * len(Menu_Makanan)
jumlah_pemesanan_minuman = [0] * len(Menu_Minuman)
jumlah_pemesanan_tambahan = [0] * len(Tambahan)
pemesanan_makanan = True
x = True
pemesanan_minuman = True
y = True

while pesan:
    print("Selamat Datang Di Cinto Bundo!")
    print("----------------------------------------------------------------")

    # Menu Makanan
    print("|Menu Makanan|")
    print("========================================")
    for i in range(len(Menu_Makanan)):
        print(f"|{i + 1}.| {Menu_Makanan[i]:18}|   Rp{Harga_Makanan[i]:7}   |")
    print ("========================================")

    # Pemesanan Makanan
    while pemesanan_makanan:
        x = True
        pesanan_makanan = int(input("Pilih Makanan (0 untuk selesai): "))
        if 1 <= pesanan_makanan <= len(Menu_Makanan):
            print(f"Anda Telah Memilih: {Menu_Makanan[pesanan_makanan - 1]}")
            jumlah_pesan_makanan = int(input("Mau mesen berapa : "))
            jumlah_pemesanan_makanan[pesanan_makanan - 1] += jumlah_pesan_makanan  
        elif pesanan_makanan == 0:
            pemesanan_makanan = False
            x = False  
        else:
            print("Tidak ada Makanan yang tersedia!")
        while x:
            konfirmasi_pemesanan_makanan = input("Apakah ingin menambah makanan lagi? (y/n): ")
            while (konfirmasi_pemesanan_makanan != "y" and konfirmasi_pemesanan_makanan != "n"):
                print("Silahkan mengisi y (jika ya) atau n (jika tidak) saja")
                konfirmasi_pemesanan_makanan = input("Apakah Anda ingin memesan makanan lagi? (y/n): ")
            if konfirmasi_pemesanan_makanan == "n":
                pemesanan_makanan = False
                x = False
            else:
                x = False

    # Menu Minuman
    print("\n|Menu Minuman|")
    print("========================================")
    for i in range(len(Menu_Minuman)):
        print(f"|{i + 1}.|   {Menu_Minuman[i]:18}   | Rp{Harga_Minuman[i] : 7}|")
    print("========================================")
    # Pemesanan Minuman
    
    while pemesanan_minuman:
        y = True # Tujuannya agar dapat masuk ke while x lagi untuk menanyakan customer apakah ingin memesan lagi
        pesanan_minuman = int(input("Pilih Minuman (0 untuk selesai): "))
        if 1 <= pesanan_minuman <= len(Menu_Minuman):
            print(f"Anda Telah Memilih: {Menu_Minuman[pesanan_minuman - 1]}")
            jumlah_pesan_minuman = int(input("Mau mesen berapa : "))
            jumlah_pemesanan_minuman[pesanan_minuman - 1] += jumlah_pesan_minuman  
        elif pesanan_minuman == 0:
            pemesanan_minuman = False
            y = False  
        else:
            print("Tidak ada Minuman yang tersedia!")
        while y:
            konfirmasi_pemesanan_minuman = input("Apakah ingin menambah minuman lagi? (y/n): ")
            while (konfirmasi_pemesanan_minuman != "y" and konfirmasi_pemesanan_minuman != "n"):
                print("Silahkan mengisi y (jika ya) atau n (jika tidak) saja")
                konfirmasi_pemesanan_minuman = input("Apakah Anda ingin memesan minuman lagi? (y/n): ")
            if konfirmasi_pemesanan_minuman == "n":
                pemesanan_minuman = False
                y = False
            else:
                y = False

    # Menu Tambahan
    print("\n|Menu Tambahan|")
    print("====================================")
    for i in range(len(Tambahan)):
        print (f"|{i + 1}.| {Tambahan[i]:18} | Rp{Harga_Tambahan[i]:7}|")
    print("====================================")

    # Pemesanan Tambahan
    konfirmasi_tambahan = input("Apakah Anda ingin memesan tambahan? (y/n): ")
    while (konfirmasi_tambahan != "y" and konfirmasi_tambahan != "n"):
        print("Silahkan mengisi y (jika ya) atau n (jika tidak) saja")
        konfirmasi_tambahan = input("Apakah Anda ingin memesan tambahan? (y/n): ")

    if konfirmasi_tambahan == "y":
        while True:
            pesanan_tambahan = int(input("Pilih Menu Tambahan (0 untuk selesai): "))
            if 1 <= pesanan_tambahan <= len(Tambahan):
                print(f"Anda Telah Memilih : {Tambahan[pesanan_tambahan - 1]}")
                jumlah_pesan_tambahan = int(input("Mau mesen berapa? "))
                jumlah_pemesanan_tambahan[pesanan_tambahan - 1] += jumlah_pesan_tambahan  
            elif pesanan_tambahan == 0:
                break  
            else:
                print("Tidak ada Tambahan yang tersedia!")

            konfirmasi_pemesanan_tambahan = input("Apakah ingin menambah tambahan lagi? (y/n): ")
            while (konfirmasi_pemesanan_tambahan != "y" and konfirmasi_pemesanan_tambahan != "n"):
                print("Silahkan mengisi y (jika ya) atau n (jika tidak) saja")
                konfirmasi_pemesanan_tambahan = input("Apakah Anda ingin memesan tambahan? (y/n): ")
            if konfirmasi_pemesanan_tambahan == "n":
                break

    # Tampilkan Ringkasan Pesanan
    print("\nRingkasan Pesanan:")
    total_harga = 0
    print("Makanan:")
    for i in range(len(Menu_Makanan)):
        if jumlah_pemesanan_makanan[i] > 0:
            print("======================================================")
            print("| Menu Makanan         | Jumlah       |     Harga    |")
            print("|----------------------|--------------|--------------|")
            print(f"| {Menu_Makanan[i]:<20} | {jumlah_pemesanan_makanan[i]:<12} | Rp{Harga_Makanan[i] * jumlah_pemesanan_makanan[i]:<10,} |")
            print("======================================================")
            total_harga += Harga_Makanan[i] * jumlah_pemesanan_makanan[i]

    print("\nMinuman:")
    for i in range(len(Menu_Minuman)):
        if jumlah_pemesanan_minuman[i] > 0:
            print("======================================================")
            print("| Menu Minuman         | Jumlah       |     Harga    |")
            print("|----------------------|--------------|--------------|")
            print(f"| {Menu_Minuman[i]:<20} | {jumlah_pemesanan_minuman[i]:<12} | Rp{Harga_Minuman[i] * jumlah_pemesanan_minuman[i]:<10,} |")
            print("======================================================")
            total_harga += Harga_Minuman[i] * jumlah_pemesanan_minuman[i]

    print("\nTambahan:")
    for i in range(len(Tambahan)):
        if jumlah_pemesanan_tambahan[i] > 0:
            print("======================================================")
            print("| Menu Tambahan         | Jumlah      |     Harga    |")
            print("|----------------------|--------------|--------------|")
            print(f"| {Tambahan[i]:<20} | {jumlah_pemesanan_tambahan[i]:<12} | Rp{Harga_Tambahan[i] * jumlah_pemesanan_tambahan[i]:<10,} |")
            print("======================================================")
            total_harga += Harga_Tambahan[i] * jumlah_pemesanan_tambahan[i]

    print(f"\nTotal Harga: Rp{total_harga}")
    print()
    # Memilih metode pembayaran 
    print("----------------------------------------------------------------")
    print("1. Kartu Kredit")
    print("2. Transfer Bank")
    print("3. E-Wallet") 
    print("4. Tunai")
    print()
    N = int(input("Pilih metode pembayaran yang Anda inginkan : "))   

    while (N < 1 or N > 4):
        print("Pilihan tidak valid, silahkan masukkan pilihan yang valid")
        N = int(input("Pilih metode pembayaran yang Anda inginkan : "))
    
    if(N == 1):
        print("=== Anda memilih pembayaran dengan Kartu Kredit ===")
        print("Silahkan melanjutkan pembayaran Anda di kasir")
        print()
        print("Terima kasih sudah makan di Cinto Bundo")
    elif(N == 2):
        print("=== Anda memilih pembayaran dengan Transfer Bank ===")
        print("Silahkan mentransfer dengan bank pilihan Anda")
        print()
        print("Terima kasih sudah makan di Cinto Bundo")
    elif(N == 3):
        print("=== Anda memilih pembayaran dengan E-Wallet ===")
        print("Silahkan membayar dengan men-scan QRIS yang terdapat di kasir")
        print()
        print("Terima kasih sudah makan di Cinto Bundo")
    else: # N == 4
        print("=== Anda memilih pembayaran dengan Tunai ===")
        Bayar = int(input("Anda ingin membayar dengan nominal berapa : "))

        while Bayar < total_harga:
            kurang = total_harga - Bayar
            print(f"Mohon maaf, pembayaran Anda masih kurang Rp{kurang}")
            print("Silahkan masukkan nominal yang lebih besar atau sama dengan harga total")
            Bayar = int(input("Anda ingin membayar dengan nominal berapa : "))

        if Bayar == total_harga:
            print()
            print("Terima kasih sudah makan di Cinto Bundo")
        else:
            sisa = Bayar - total_harga
            print(f"Kembalian Anda adalah Rp{sisa}")
            print()
            print("Terima kasih sudah makan di Cinto Bundo")
    print()
    print("Kami dari pihak Resto Cinto Bundo izin meminta waktu 1 menit agar Bapak/Ibu dapat memberikan penilaian mengenai pelayanan kami")
    penilaian = str(input("Silahkan berikan kritik dan saran agar dapat membantu meningkatkan pelayanan kami: "))
    rating = int(input("Harap berikan rating dari 1 sampai 5: "))
    while rating < 1 or rating > 5:
        print("Tolong masukkan angka dari 1 sampai 5 : ")
        rating = int(input("Harap berikan rating dari 1 sampai 5: "))
        
    print(f"Anda memberikan {rating} bintang")
    print()
    print("Terima kasih telah meluangkan waktu Bapak/Ibu untuk mengevaluasi pelayanan kami")




   
