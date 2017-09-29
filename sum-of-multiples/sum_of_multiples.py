def sum_of_multiples(num, mltpls):
    sum_list = []
    for n in mltpls:
        sum_list.append(list(range(n, num, n)))
    answer = [ x for sub_list in sum_list for x in sub_list ] 
    final = set(answer)
    
    return sum(final)
