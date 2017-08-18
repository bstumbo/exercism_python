import collections

def is_isogram(word):
    
    # Use collection counter to count number of repeating letters in lower case of word
    
    results = collections.Counter(word.lower())
    
    # Iterate over collection to see if value is more than 1
    # Also checks that character is alpha
    # if count is > 1, returns false
    
    for s, v in results.items():
        if v > 1 and s.isalpha():
            return False

    return True