stack = []

def tambah_barang (stack, barang_baru):
    stack.append(barang_baru)
    print(f" {barang_baru} berhasil ditambahkan ke dalam stack.")

def hapus_barang_terakhir(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang dapat dihapus.") 
    else:
        barang_terakhir = stack.pop()
        print(f"{barang_terakhir} nerhasil dihapus dari stack.")

def tampilkan_barang_teratas(stack):
    if len(stack) == 0:
        print("Stack kosong, tidak ada barang yang dapat ditampilkan.")
    else:
        barang_teratas = stack[-1]
        print(f"Barang teratas didalam stack adalah {barabf_teratas}.")

while True:
    print("\nGudang saat ini:", stack)
    print("Menu")
    print("1. Tamabah barang")
    print("2. Hapus barang terakhir")
    print("3. Tampilkan barang teratas")
    print("4. Keluar")

    pilihan = input("Masukkan pikihab anda (1/2/3/4): ")

    if pilihan == "1" :
        barang_baru = input("Masukkan nama barang yang akan ditambahakan: ")
        tambah_barang(stack, barang_baru)

    elif pilihan == "2":
        hapus_barang_terakhir(stack)
    elif pilihan == "3":
        tampilkan_barang_teratas(stack)
    elif pilihan == "4":
        print("Terimakasih telah menggunakan prohram ini") 
        break
    else:
        print("Pilihan tidak valid. Silahkan masukan pilihan yang benar.")           
