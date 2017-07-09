ORIG_COOKIE = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4oExFZaAw='
GUESSED_JSON = '{"showpassword:"}'

XOR_KEY = "qw8J" # solved with print_xor_key
HACKY_COOKIE = '{"showpassword":"yes","bgcolor":"#ffbbfa"}'

def print_xor_key():
	"""
	GUESSED_JSON is shorter than the cookie length so an exception is thrown but
	the xor_key is short enough to calculate from the data we get.
	"""
	xor_key = ""
	non_base64 = ORIG_COOKIE.decode("base64")
	
	try:
		for index, i in enumerate(non_base64):
			xor_key += chr(ord(i) ^ ord(GUESSED_JSON[index]))
	except Exception:
		pass
	print xor_key
	
def print_original_cookie():
	"""
	Used to confirm xor key
	"""
	non_base64 = ORIG_COOKIE.decode("base64")
	print "".join([chr(ord(i) ^ ord(XOR_KEY[index % 4])) for index, i in enumerate(non_base64)])

def create_hacky_cookie():
	"""
	Create hacky cookie
	"""
	xored = "".join([chr(ord(i) ^ ord(XOR_KEY[index % 4])) for index, i in enumerate(HACKY_COOKIE)])
	print xored.encode("base64")
		
create_hacky_cookie()
