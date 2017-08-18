import re

def decode(d_string):
    
    return ''.join(
        int(count) * letter if count else letter
        for count, letter in re.findall('(\d*)(.)', d_string))

def encode(e_string):
   return ''.join(
        "%d%s" % (len(letters), letter) if len(letters) > 1 else letter
        for letters, letter in re.findall(r'((.)\2*)', e_string))
