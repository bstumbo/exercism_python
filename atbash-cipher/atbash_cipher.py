import string
import re

def encode(s_encode):
    alpha = list(string.ascii_lowercase)
    cipher = list(reversed(alpha))
    build_string = ""
    count = 0
    s_encode = re.sub('[^0-9a-zA-Z]+', '', s_encode)
    
    for s in list(s_encode.replace(" ", "").lower()):
        if count == 5:
            if s.isalpha():
                build_string += " " + cipher[alpha.index(s)]
                count = 1
            else:
                build_string += s
                count = 1
        else:
            if s.isalpha():
                build_string += cipher[alpha.index(s)]
                count += 1
            else:
                build_string += s
                count += 1
    
    return build_string

def decode(s_decode):
    alpha = list(string.ascii_lowercase)
    cipher = list(reversed(alpha))
    build_string = ''
    s_decode = re.sub('[^0-9a-zA-Z]+', '', s_decode)
    
    for s in list(s_decode.replace(" ", "").lower()):
        if s.isalpha():
            build_string += alpha[cipher.index(s)]
        else:
            build_string += s
            
    return build_string