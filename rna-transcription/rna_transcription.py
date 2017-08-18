def to_rna(input):
   
    convert_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    
    #Create new list
    
    rna_list = ''.join(( convert_dict.get(v, '') for v in input))
    
    if len(rna_list) == len(input):
        return rna_list
    else:
        return ''
    
    
    
