import collections

def detect_anagrams(word, candidates):
    breakdown = collections.Counter(word.lower())
    answer = []
    for i in candidates:
        if i.lower() != word and i.title() != word.title() and collections.Counter(i.lower()) == breakdown:
            answer.append(i)
            
    return answer
    

candidates = ["cashregister", "carthorse", "radishes"]     
test = detect_anagrams("Orchestra", candidates)
print(test)
