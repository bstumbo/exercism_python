import collections
import re

def word_count(string):
    
    cnt = collections.Counter()
    stripped = re.sub(r'([^\s\w]|_)+', ' ', string)
    
    for word in stripped.lower().split():
        cnt[word] += 1
    
    return cnt
