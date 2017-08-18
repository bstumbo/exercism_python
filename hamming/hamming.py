def distance(a, b):
        
    if len(a) != len(b): raise ValueError('Strands must be the same length')
    return len([1 for (s1, s2) in zip(a, b) if s1 != s2])

