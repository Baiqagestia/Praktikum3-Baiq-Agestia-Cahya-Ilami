print("="*30)
print("PROGRAM KONTAK BY BAIQ AGESTIA")
print("="*30)

def tampilkan_menu():
    print("\n=== Menu Kontak ===")
    print("1. Tambah Kontak")
    print("2. Cari Kontak")
    print("3. Hapus Kontak")
    print("4. Tampilkan Semua Kontak")
    print("5. Keluar")

def main():
    # Dictionary untuk menyimpan data kontak
    kontak = {}

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama kontak: ").title()
            nomor = input("Masukkan nomor telepon: ")
            kontak[nama] = nomor
            print(f"Kontak '{nama}' berhasil ditambahkan.")

        elif pilihan == "2":
            nama = input("Masukkan nama yang ingin dicari: ").title()
            if nama in kontak:
                print(f"Nomor telepon '{nama}' adalah {kontak[nama]}")
            else:
                print(f"Kontak '{nama}' tidak ditemukan.")

        elif pilihan == "3":
            nama = input("Masukkan nama kontak yang ingin dihapus: ").title()
            if nama in kontak:
                del kontak[nama]
                print(f"Kontak '{nama}' berhasil dihapus.")
            else:
                print(f"Kontak '{nama}' tidak ditemukan.")

        elif pilihan == "4":
            if kontak:
                print("\nDaftar Semua Kontak:")
                for nama, nomor in kontak.items():
                    print(f"- {nama}: {nomor}")
            else:
                print("Belum ada kontak yang tersimpan.")

        elif pilihan == "5":
            print("Terima kasih telah menggunakan program kontak!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-5.")

if __name__ == "__main__":
    main()
