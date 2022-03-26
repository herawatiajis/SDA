barang = []
pilihan = 0

while pilihan !=7:
    print('''menu pilihan :
          1. menambah barang
          2. menghapus barang
          3. mengedit barang
          4. menampilkan isi barang
          5. mencari barang
          6. menampilkan index barang tertentu
          7. Exit''')
    
    pilihan = int(input('masukkan menu pilihan :'))
    
    if pilihan == 1:
        tambah = input('masukkan barang :')
        barang.extend(tambah.split(','))
    
    elif pilihan == 2:
        while True:
            hapus = int(input('masukkan index barang yang akan di hapus :'))
            if hapus > len(barang):
                print('masukkan index dengan benar !')
            else:
                barang.pop(hapus)
                
                lanjut = input('ketik y jika ingin lanjut selain y brhenti :').lower()
                if lanjut != 'y':
                    break
                
    elif pilihan == 3:
        while True:
            edit = int(input('masukkan index yang akan di edit :'))
            if edit > len(barang):
                print('barang yang ingin diedit tdk tersedia')
            else:
                barang [edit] = input('masukkan nama barang :')
            
                lanjut = input('ketik y jika ingin lanjut selain y brhenti :').lower()
                if lanjut != 'y':
                    break 
                
    elif pilihan == 4:
        for i in barang:
            print(i) 
            
    elif pilihan == 5:
        cari = input('masukkan barang yang dicari :')
        for i in range(len(barang)):
            if barang[i] == cari:
                print('barang di temukan')
            else:
                print('barang tidak di temukan') 
                
    elif pilihan == 6:
        cari_index = input('masukkan nama barang :')
        
        if cari_index in barang:
            print(cari_index,'berada pada index ke-',barang.index(cari_index))
        else:
            print('barang tidak tersedia')
print(barang)