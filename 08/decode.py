ENC_SEC = "3d3d516343746d4d6d6c315669563362"

hex_array = ["0x" + str(ENC_SEC[i:i+2]) for i in xrange(0, len(ENC_SEC), 2)]

print "".join([chr(int(i, 16)) for i in hex_array])[::-1].decode("base64")
