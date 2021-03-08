from os import system, name
import smtplib
import getpass
import time
import ssl
import sys

def clear():
	if name == 'nt':
		_ = system("cls")
	else:
		_ = system("clear")

def StartUp():
	clear()
	print("""

 /██      /██           /██ /██ /███████                          /██      
| ███    /███          |/_/| ██| ██__ /██                        | ██     
| ████  /████  /██████  /██| ██| ██  \ ██  /██████  /██████/████ | ███████ 
| ██ ██/██ ██ |/____/██| ██| ██| ███████  /██__ /██| ██_ /██_ /██| ██__ /██
| ██  ███| ██  /███████| ██| ██| ██__ /██| ██  \ ██| ██ \ ██ \ ██| ██  \ ██
| ██\  █ | ██ /██___/██| ██| ██| ██  \ ██| ██  | ██| ██ | ██ | ██| ██  | ██
| ██ \/  | ██|  ███████| ██| ██| ███████/|  ██████/| ██ | ██ | ██| ███████/
|/_/     |/_/ \_______/|/_/|/_/|/______/  \______/ |/_/ |/_/ |/_/|/______/ 
	""")
	UserInfo()

def UserInfo():
	global user, passwd, to, body, sub, times, secs, txt, msg

	pick = input("\n[?] 1. Enter Info/2. Import from file: ")
	if pick == "1":
		print("\n[+] Login Info")
		user = input("[?] Email: ")
		passwd = getpass.getpass("[?] Password: ")

		print("\n[+] Send Info")
		to = input("[?] To: ")
		sub = input("[?] Subject: ")
		body = input("[?] Message: ")

		print("\n[+] Settings")
		times = input("[?] Times sent?: ")
		secs = input("[?] Secconds between sends?: ")
		txt = input("[?] Save settings to .txt file Y/N?: ")

		if txt == "y":
			print("\n[+] Write to file")
			filen = input("[?] File name (Include file extention): ")

			system("touch " + filen)
			f = open(filen, "w")
			f.writelines(user + "\n" + passwd + "\n" + to + "\n" + sub + "\n" + body + "\n" + times + "\n" + secs)
			f.close()

			print("\n[+] Options writen to " + filen)
			msg = 'From: ' + user + '\nSubject: ' + sub + '\n' + body
			MainScript()

		elif txt == "n":
			msg = 'From: ' + user + '\nSubject: ' + sub + '\n' + body
			MainScript()

	elif pick == "2":
		filen = input("\n[?] Enter file name with file extention: ")

		f = open(filen, "r")
		line = f.readlines()

		user = line[0]
		passwd = line[1]
		to = line[2]
		sub = line[3]
		body = line[4]
		times = line[5]
		secs = line[6]

		f.close()
		msg = 'From: ' + user + 'Subject: ' + sub + '\n' + body
		MainScript()

	elif pick == "exit":
		print("\n[!] Exiting now...")
		sys.exit()

	else:
		print("\n[!] Input unreconized")
		UserInfo()

def MainScript():
	server = smtplib.SMTP(host='smtp.gmail.com', port=587)
	server.starttls()
	server.login(user, passwd)
	print("")

	for i in range(1, int(times)+1):
		server.sendmail(user, to, msg)
		print("\r[+] E-mails sent: " + str(i))
		time.sleep(int(secs))

	server.quit()
	print("\n[+] Process done!")
	UserInfo()

StartUp()