def sieve(top):
    range_list = list(range(2, top + 1))
    
    unprime = []
    prime = []
    
    for i in range_list:
        if i not in unprime:
            prime.append(i)
            for j in list(range(i*i, top +1, i)):
                unprime.append(j)
    return prime
