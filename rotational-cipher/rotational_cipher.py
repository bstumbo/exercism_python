import string

def rotate(letter, shift):
    abc_low = list(string.ascii_lowercase)
    abc_cap = list(string.ascii_uppercase)
    build_string = ''   
    
    for s in list(letter):
        if s.isupper():
            build_string += abc_cap[(abc_cap.index(s) + shift) % len(abc_cap)] 
        
        elif s.islower():
            build_string += abc_low[(abc_low.index(s) + shift) % len(abc_low)] 
        
        else:
            build_string += s
        
    return build_string
