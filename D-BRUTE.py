import os
import time
import sys
import colorama
from colorama import Fore, Back, Style
import readline


try:
	import readline
except ImportError:
	import pyreadline as readline

CMD = ["menü", "clear","exit",  ]
def completer(text, state):
	options = [cmd for cmd in CMD if cmd.startswith(text)]
	if state < len(options):
		return options[state]
	else:
		return None

readline.parse_and_bind("tab: complete")
readline.set_completer(completer)











RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
PINK="\033[35m"
CYAN="\033[36m"
WHITE="\033[37m"
NORMAL="\033[0;39m"

PURPLE = '\033[95m'
CYAN = '\033[96'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
NORMAL= '\033[0;39m'


def main():
	os.system("bash src/banner.sh")
	print("")
	print("\033[1m   \033[91m[\033[0;39m\033[1m1\033[91m]\033[0;39m\033[1m SSH Brute Force Saldırısı\033[0;39m")
	print("\033[1m   \033[91m[\033[0;39m\033[1m2\033[91m]\033[0;39m\033[1m FTP Brute Force Saldırısı\033[0;39m")
	print("\033[1m   \033[91m[\033[0;39m\033[1m3\033[91m]\033[0;39m")
	print("\033[1m   \033[91m[\033[0;39m\033[1m4\033[91m]\033[0;39m")
	print("\033[1m   \033[91m[\033[0;39m\033[1m5\033[91m]\033[0;39m")
	print("")

dbrute = "1"
main()

while dbrute == "1":
	dbinput= input("\033[1m\033[91mroot@dbrute\033[0;39m\033[1m:\033[94m~\033[0;39m\033[1m# ")

	if (dbinput == "clear"):
		os.system("clear")


	elif (dbinput == "menü"):
 		main()

	elif (dbinput == "exit"):

		print("\033[1mÇıkılıyor /")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor -")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor |")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor /")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor -")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor |")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor /")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor -")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor |\033[0;39m")
		time.sleep(0.3)
		os.system("clear")
		print("\033[1mÇıkılıyor /")
		os.system("clear")

		break
	elif (dbinput == "1"):
		os.system("python3 src/ssh/brute_force_password.py")
	



















