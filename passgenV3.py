#coded by cybereagle2001

import random
import os
from time import sleep

char="abcdefjhigklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-.!%:;,.?µ=+}])°[({'#~&0123456789"

def banner():
    print("@AllRightReserved to cybereagle2001")
    print("\033[1;34m  _ __   __ _ ___ ___  __ _  ___ _ __")
    print("|  _ \ / _  / __/ __|/ _  |/ _ \  _ \"")
    print("| |_) | (_| \__ \__ \ (_| |  __/ | | |")
    print("| .__/ \__,_|___/___/\__, |\___|_| |_|")
    print("|_|                  |___/cybereagle2001 ")
    print("\033[1;37m")
    
def main():
    for c in range(100):
        password=''
        for loop in range(n+1):
            password += random.choice(char)
        file = open("password.txt","a")
        file.write(password+"\n")
        file.close()
        print(password)
        sleep(0.2)

    print("")
    print("\033[1;31mStay Secure with cybereagle2001 random passwords!!")
    
def verif(n):
    if (n < 10):
        os.system("clear")
        banner()
        print("the minimum length for a secure password is 10 caracters!!\n")
        n= int(input("write the length of your password:"))
        verif(n)
    else:
        main()
    
banner()
n=int(input("write the length of your password: "))
verif(n)

