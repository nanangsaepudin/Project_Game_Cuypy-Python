from libs import welcome_message, exit_program
from games import cuypy
from tools import warung


def menu():
    user_options = int(input(f'\nMenu pilihan:\n1. Game CUYPY\n2. Warung mini\n3. Keluar program\n\nsilahkan pilih menunya : '))
    if user_options == 1:
        cuypy.start()
    elif user_options == 2:
        warung.start()
    elif user_options == 3:
        exit_program()
    else:
        print ("Menu tidak tersedia")



def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()