import main

def start():
    while True:
        print("\nPilih kategori")
        print("1. Makanan")
        print("2. Minuman")
        print()

        pilih = int(input("Kamu milih (1/2) : "))

        if pilih == 1:
            print("1. Nasi Goreng (Rp 15.000)")
            print("2. Ayam Goreng (Rp 18.000)")
            print()

            menu = int(input("Kamu mau pilih makanan yang mana (1/2) : "))

            if menu == 1:
                porsi = int(input("Mau berapa porsi : "))
                total = porsi * 15000
                print("Total yang harus kamu bayar : Rp", total , "\n")

            elif menu == 2:
                porsi = int(input("Mau berapa porsi : "))
                total = porsi * 18000
                print("Total yang harus kamu bayar : Rp", total , "\n")

            else:
                print("Makanan tidak tersedia")

        elif pilih == 2:
            print("1. Es Teh (Rp 5.000)")
            print("2. Kopi   (Rp 8.000)")
            print()

            menu = int(input("Kamu mau pilih minuman yang mana (1/2) : "))

            if menu == 1:
                porsi = int(input("Mau berapa porsi : "))
                total = porsi * 5000
                print("Total yang harus kamu bayar : Rp", total, "\n")

            elif menu == 2:
                porsi = int(input("Mau berapa porsi : "))
                total = porsi * 8000
                print("Total yang harus kamu bayar : Rp", total, "\n")

            else:
                print("Minuman tidak tersedia")

        else:
            print("Menu tidak tersedia")

        play_again = input('kembali ke menu [y/n]: ')
        
        if play_again == "y":
            main.menu()
        
    
    
if __name__ == '__main__':
    start()
