import socket
from time import sleep
import sys


def welcome_message():
    print("Selamat Datang Di Game Cuypy")
    nama = input("Masukkan nama anda : ")
    style = "*" * (len(nama) + 6)
    print(style)
    print(f"** {nama} **")
    print(style)
    
def exit_program():
    print('Program akan dihentikan')
    sleep(1)
    print('3...')
    sleep(1)
    print('2...')
    sleep(1)
    print('1...')
    sleep(1)
    print('Program berhasil dihentikan')
    sys.exit()
    
    
if __name__ == '__main__':
    exit_program()

