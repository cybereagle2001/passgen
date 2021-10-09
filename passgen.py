#coded by cybereagle2001

import random
from time import sleep

char="abcdefjhigklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/*-.!%:;,.?µ=+}])°[({'#~&"

print("@AllRightReserved to cybereagle2001")
print("\033[1;34m  _ __   __ _ ___ ___  __ _  ___ _ __")
print("|  _ \ / _  / __/ __|/ _  |/ _ \  _ \"")
print("| |_) | (_| \__ \__ \ (_| |  __/ | | |")
print("| .__/ \__,_|___/___/\__, |\___|_| |_|")
print("|_|                  |___/cybereagle2001 ")
print("\033[1;37m")
n=int(input("write the length of your password: "))
for c in range(100):
    password=''
    for loop in range(n):
        password += random.choice(char)
    file = open("password.txt","a")
    file.write(password+"\n")
    file.close()
    print(password)
    sleep(0.2)

print("")
print("\033[1;31mStay Secure with cybereagle2001 random passwords!!")