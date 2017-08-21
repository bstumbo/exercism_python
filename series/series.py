def slices(nums, digits):
    list_build = []
    answer = []

    for i, v in enumerate(list(nums)):
        if len(list(nums[i:i + digits])) == digits:
            list_build.append(list(nums[i:i + digits]))
            
    for item in list_build:
        answer.append(list(map(int, item)))
    
    if not answer:
        raise ValueError("Oh no, something went wrong!")
    
    for x in answer:
        if len(x) == 0:
            raise ValueError("Busted")
         
    return answer
