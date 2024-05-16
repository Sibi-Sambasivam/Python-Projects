import requests


target_url = input('Enter Target URL:')
file_name = input('Enter the name of the file containing directories:')


def request(url):
	try:
		return requests.get("http://" + url)
	except requests.exceptions.ConnectionError:
		pass


file = open(file_name, 'r')
for line in file:
	directory = line.strip()
	full_url = target_url
	response = request(full_url)
	if response:
		print(' Discovered directory at this path: ' + full_url)