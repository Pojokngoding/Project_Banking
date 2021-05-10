import random, string
balik = 'y'
while (balik == 'y'):
        print("* SELAMAT DATANG DI NF BANK *")
        print("--------------------------------------------------------")  #pemisah
        print("Menu : ")
        print("[1] Buka Rekening ")
        print("[2] Setoran Tunai")
        print("[3] Tarik Tunai ")
        print("[4] Transfer ")
        print("[5] Lihat Daftar Transfer")
        print("[6] Cek Saldo ")
        print("[7] Keluar ")
        print("--------------------------------------------------------")  #pemisah
        menu = input(" Masukan Pilihan Anda : ")

        #MENU 1
        if menu == "1": # Jika Pilihannya adalah angka  1 ,alias Menu 1 
            print("* BUKA REKENING *") # Cetak Buka Rekening
            nama = input("Masukan Nama : ") # Masukan Nama Nasabah
            setoran = int(input("Masukan Setoran Awal : ")) # Masukan Dana awal
            norek = "REK" + ''.join(random.choice(string.digits) for _ in range(3))
            #  memanfaatkan modul random dan string. untuk membuat kode nasabah
            print("Pembukaan rekening dengan nomor", norek, "atas nama", nama,"berhasil")
            # Jika Inputan Nama dan Setoran awal selesai dan benar Maka  
            fwrite = open('nasabah.txt', 'a')
            # Membuka file nasabah.txt , jika belum nanti automatis terbuat file nasabah.txt
            fwrite.write(norek+','+nama+','+ str(setoran)+'\n')
            # Menulis Norek , nama nasabah serta setoran dana awal
            fwrite.close()
            # setelah selesai file text harus ditutup
        #MENU 2
        elif menu == "2": # Jika Pilihannya adalah angka 2 , alias Menu 2
            print("*** SETORAN TUNAI ***") # Cetak Setoran Tunai
            data_nasabah = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            data_nasabah2 = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            nomor_rek = input("Masukan Rekening : ") # Membuat variable yang menyimpan nomor rekening
            nominal = int(input("masukan nominal yang akan disetor : ")) # Membuat variable yang menyimpan bilangan integer
            nomor_rek = nomor_rek.upper() 
            # Jika karakter string pada variable nomor_rek kecil maka akan diubah menjadi kapital
            fwrite = open('nasabah.txt') # buka file nasabah.txt
            for i in fwrite : # Membuat perulangan pada variable fwrite
                data = i.split(",") # Mengubah isi dari i menjadi list dengan separator koma menggunakan method split
                data_nasabah.append([data[0],data[1],int(data[2])]) # Membuat list multidimensi dengan meng-append setiap indeks variable data ke variable data_nasabah
            for i in data_nasabah : # Membuat perulangan pada variable data_nasabah
                for j in i : # Membuat perulangan pada variable i dari perulangan sebelumnya
                    data_nasabah2.append(j) # Membuat list dengan meng-append setiap perulangan pada j ke variable data_nasabah2
            if nomor_rek in data_nasabah2 : # Program akan lanjut jika  variable nomor_rek berada di dalam variable data_nasabah2
                for i in data_nasabah : # Membuat perulangan pada variable data_nasabah 
                    if i[0] == nomor_rek : # program akan lanjut jika indeks 0 pada i yaitu nomor rekening "REKxxx" sama dengan variable nomor_rek
                        i[2] += nominal # menjumlahkan indeks 2  pada i dengan variabel nominal 
                        with open("nasabah.txt", "w") as fwrite :
                             # Membuka file nasabah.txt dengan sebagai variable fwrite dengan mode w untuk menulis
                            fwrite.write(
                                "\n".join(map(lambda x : ",".join(map(str, x)),  data_nasabah)))
                                 # Mengganti indeks 2 pada variabel data_nasabah dengan hasil penjumlahan sebelumnya menggunakan lambda Expression
                        fwrite.close()
                        print("Setoran tunai sebesar", nominal, "ke rekening", nomor_rek, "berhasil.")
                        break # Menghentikan perulangan for
            elif nomor_rek in data_nasabah2 < 50000:
                print("Saldo tidak mencukupi. Tarik tunai gagal.")
            else: # Jika variable nomor_rek di input selain dengan yang ada di variable data_nasabah2 
                print("Nomor rekening tidak terdaftar. Setoran tunai gagal.")
                # maka akan mencetak "Nomor rekening tidak terdaftar. Setoran tunai gagal.""
        #MENU 3
        elif menu == "3": # Jika Pilihannya adalah angka 3 , alias Menu 3
            print("*** SETORAN TUNAI ***") # Cetak Setoran Tunai
            data_nasabah = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            data_nasabah2 = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            nomor_rek = input("Masukan Rekening : ") # Masukan Nomor Rek
            nominal = int(input("Masukkan nominal yang akan ditarik : ")) # Masukan Nominal yang ditarik " Harus bertipe data Integer "
            nomor_rek = nomor_rek.upper() # Jika karakter string pada variable nomor_rek kecil maka akan diubah menjadi kapital
            fwrite = open('nasabah.txt') # Membuka file nasabah dengan variable fwrite
            for i in fwrite :  # Membuat perulangan pada variable fwrite
                data = i.split(",") # Mengubah isi dari i menjadi list dengan separator koma menggunakan method split
                data_nasabah.append([data[0],data[1],int(data[2])])
                # Membuat list multidimensi dengan meng-append setiap indeks variable data ke variable data_nasabah
            for i in data_nasabah : # Membuat perulangan pada variable data_nasabah
                for j in i : # Membuat perulangan pada variable i dari perulangan sebelumnya
                    data_nasabah2.append(j) # Membuat list dengan meng-append setiap perulangan pada j ke variable data_nasabah2
            if nominal > i[2]: # jika variabel nominal lebih besar dari indeks 2 pada i
                print("Saldo tidak mencukupi. Tarik tunai gagal.")
                break  # Menghentikan perulangan for
            if nomor_rek in data_nasabah2 : # Program akan lanjut jika  variable nomor_rek berada di dalam variable data_nasabah2
                for i in data_nasabah :  # Membuat perulangan pada variable data_nasabah
                    if i[0] == nomor_rek :  # program akan lanjut jika indeks 0 pada i yaitu nomor rekening "REKxxx" sama dengan variable nomor_rek
                        i[2] -= nominal # Pengurangan indeks 2  pada i dengan variabel nominal 
                        with open("nasabah.txt", "w") as fwrite : # Membuka file nasabah.txt dengan sebagai variable fwrite dengan mode w untuk menulis
                            fwrite.write(
                                "\n".join(map(lambda x : ",".join(map(str, x)),  data_nasabah)))
                                # Mengganti indeks 2 pada variabel data_nasabah dengan hasil penjumlahan sebelumnya menggunakan lambda Expression
                        fwrite.close()
                        print("Tarik tunai sebesar", nominal, "ke rekening", nomor_rek, "berhasil.")
                        break # Menghentikan perulangan for
            else: # Jika variable nomor_rek di input selain dengan yang ada di variable data_nasabah2
                print("Nomor rekening tidak terdaftar. Tarik tunai gagal.")
                # maka akan mencetak "Nomor rekening tidak terdaftar. Setoran tunai gagal."
        #MENU 4
        elif menu == "4": # Jika Pilihannya adalah angka 4 , alias Menu 4
            print("* SETORAN TUNAI *")
            data_nasabah = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            data_nasabah2 = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            data_nasabah3 = [] # Membuat variable list kosong sebagai tempat penyimpanan dari method append nanti
            nomor_rek = input("Masukan Rekening : ") # Masukan Nomor Rekening
            nomor_tuj = input("Masukan Tujuan : ") # Masukan Rekening Tujuan
            nominal = int(input("masukan nominal yang akan disetor : ")) # Masukan nominal dengan tipe data integer
            nomor_rek = nomor_rek.upper() # Jika karakter string pada variable nomor_rek kecil maka akan diubah menjadi kapital
            fwrite = open('nasabah.txt') # Membuka file nasabah dengan variable fwrite
            for i in fwrite : 
                data = i.split(",")
                data_nasabah.append([data[0],data[1],int(data[2])])
            for i in data_nasabah :
                for j in i :
                    data_nasabah2.append(j)
                    data_nasabah3.append(j)
            if nominal > i[2]:
                print("Saldo tidak mencukupi. Tarik tunai gagal.")
            if nomor_rek in data_nasabah2 :
                for i in data_nasabah :
                    if i[0] == nomor_rek :
                        i[2] -= nominal
                        with open("nasabah.txt", "w") as fwrite :
                            fwrite.write(
                                "\n".join(map(lambda x : ",".join(map(str, x)),  data_nasabah)))
                        fwrite.close()
            if nomor_tuj in data_nasabah3 :
                for i in data_nasabah :
                    if i[0] == nomor_tuj :
                        i[2] += nominal
                        with open("nasabah.txt", "w") as fwrite :
                            fwrite.write(
                                "\n".join(map(lambda x : ",".join(map(str, x)),  data_nasabah)))
                        fwrite.close()
                        break
            else:
                    print("Nomor rekening tidak terdaftar. Setoran tunai gagal.")
            nomor_trf = "TRF" + ''.join(random.choice(string.digits) for i in range(3))
            data = [[nomor_trf, nomor_rek, nomor_tuj, str(nominal)]]
            p = open("transfer.txt", 'a+')
            s = open("nasabah.txt", "a+")
            for element in data :
                p.write(', '.join(element) + '\n')
            p.close()
            print("=========================================================")
            print("Transfer sebesar", nominal, "dari rekening", nomor_rek, "ke rekening", nomor_tuj, "berhasil", )  
        #MENU 5 
        elif menu == "5": # Jika Pilihannya adalah angka 5 , alias Menu 5
            print("*Cek Transfer*")
            s = input("Masukan sumber nomor rekening: ") # Masukan Nomor Rekening
            s = s.upper() # Jika karakter string pada variable nomor_rek kecil maka akan diubah menjadi kapital
            f = open("transfer.txt", 'r') # Membuka file nasabah dengan variable f , dan karena Fitur ini hanya cek saja maka menggunakan 'r'
            for i in f: # Membuat perulangan pada variable f
                data = i.split(',') # data yang ada pada file transfer.txt apabila datanya tidak rapih dan berantakan
                # maka menggunakan split untuk merapihkan datanya 
                if s in data[1]: # Membuat perulangan pada variable data index ke dua(0,1.....)
                    p = ''.join(i) # data transfer berbentuk list maka harus di ubah menggunakan join agar menjadi string
                    print(p, end="") # Mencetak Variabel p dan dipisahkan oleh space
                    break # Menghentikan Perulangan For
            else: # Jika Norek tidak terdata pada File Transfer 
                print("Nomor rekening sumber tidak terdaftar.")
                # Maka yang di cetak adalah hal diatas
        #MENU 6
        elif menu == "6" :
            print("*CEK SALDO*")
            cek_saldo = input("Masukan nomor rekening: ")
            cek_saldo = cek_saldo.upper()
            f = open('nasabah.txt', 'r')
            f1 = f.read()
            f2 = f1.split("\n")
            for i in f2:
                if cek_saldo in i:
                    convert = i.split(',')
                    print("=========================================================")
                    print("Kamu mempunyai saldo sebanyak:",convert[2])
                    break
            else:
                print("Nomor rekening tidak terdaftar. cek saldo gagal")
        #MENU 7
        elif menu == "7" : #  Jika Pilihannya adalah angka 7, alias Menu 7
            print("Terima kasih atas kunjungan Anda...") # Hasil Cetak yang Ditampilkan 
        else: # Jika Keluar dari atau lebih dari angka 7 
            print("Pilihan Anda salah. Ulangi!") # Hasil Cetakan yang ditampilkan
        print("=========================================================")
        balik = input("Apakah ingin melanjutkan program (y/n)? ")
        # Di sini hanya fitur perulangan yang sengaja dibuat untuk
        # Kembali lagi dari awal program jika Ketik "y" jika ketik
        #  "n" Maka Program selesai
        print("=========================================================")
        print("============= © Mahasiswa STT Nurul Fikri 2020 ==========")
        print("=========================================================")

        # © Mahasiswa STT Nurul Fikri 2020