import socket
from time import sleep
import sys

PC_NAME = socket.gethostname()

def welcome_message():
    style = "*" * (len(PC_NAME) + 6)
    print(style)
    print(f"** {PC_NAME} **")
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