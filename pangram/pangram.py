import collections
import string

def is_pangram(word):
    alpha = dict.fromkeys(string.ascii_lowercase, 0)
    results = collections.Counter(word.lower())
    
    for s, v in results.items():
        if v >= 1 and s.isalpha():
            alpha[s] = v
    
    for s, v in alpha.items():
        if v < 1:
            return False
    
    return True