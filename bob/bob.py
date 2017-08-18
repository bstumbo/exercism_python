def hey(string):
    
    answer_dict = {0 : "Sure.", 1: "Whoa, chill out!", 2: "Fine. Be that way!", 3 : "Whatever."}
    
    string = string.strip()
        
    if string.isupper():
        return answer_dict.get(1)
    if string.endswith('?'):
        return answer_dict.get(0)
    if any(s.isalpha() or s.isnumeric() for s in string):
        return answer_dict.get(3)
    else:
        return answer_dict.get(2)