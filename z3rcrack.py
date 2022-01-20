#!/usr/bin/python3


import crypt
import sys

def use_mode():
	print("|")
	print("| USE MODE: python3 z3rcrack.py")
	print("| ")
	print("| Adicional Options:  ")
	print("| ")
	print("|     --worlist | -w 	Insert worlist that will use on the crack")
	print("| ")
	print("| Exemplas: ")
	print("|     python3 hashcrack.py --wordlist myword.lst")
	print("|     python3 hashcrack.py -w myword.lst")
	print("|")
	exit(0)

if len(sys.argv) != 3:
	use_mode()

if sys.argv[1] == "--wordlist" or sys.argv[1] == "-w":
	if len(sys.argv[2]) < 0:
		wordlist = "wl.lst"
	else:
		wordlist = sys.argv[2]
else:
	print("\n| Use default wordlist..")
	wordlist = "wl.lst"

print("\n - - - - - - - - - - - - - - - - - - - - - - - ")
print("| ")
print("| Dev: Z3R0 Sh3ll")
print("| Cracking the hash, for educacional use.")
print("| Enjoy!")
print(" - - - - - - - - - - - - - - - - - - - - - - - \n")

hash = str(input("[=] Complete hash: "))
salt = str(input("[=] Sault:  "))

print("\n - - - - - - - - - - - - - - - - - - - - - - - ")
print("| Cracking....")
print(" - - - - - - - - - - - - - - - - - - - - - - - \n")

with open(wordlist, "r") as file:
	file = file.read().split('\n')
	for passwd in file:
		key = crypt.crypt(passwd, salt)

		if key == hash:
			print("\n[+] PASSWORD FOUND: %s" % passwd)
			exit(0)
		else:
			print("[-] Trying: %s" % passwd)
