class Allergies(object):
    def __init__(self, object):
        self.total = object
        self.allergy_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
        self.allergy_dict = { "eggs" : 1, "peanuts" : 2, "shellfish" : 4, "strawberries" : 8, "tomatoes" : 16, "chocolate" : 32, "pollen" : 64, "cats" : 128 }
        self.final_list = []
        
    def sum_allergy(self, allergy_list, test, partial=[], partial_sum=0):
        
        if partial_sum == test:
            yield partial
        if partial_sum >= test:
            return
        for i, n in enumerate(allergy_list):
            remaining = allergy_list[i+1:]
            yield from self.sum_allergy(remaining, test, partial + [n], partial_sum + n)
            
    def is_allergic_to(self, type):
        specific_allergy = self.allergy_dict.get(type)
        allergy_set = list(self.sum_allergy(self.allergy_list, self.total))
        
        for n in allergy_set:
            if specific_allergy in n:
                return True
            else:
                return False
            
    def lst(self):
        answer_list = []
        allergy_set = list(self.sum_allergy(self.allergy_list, self.total))
        inv_allergy = {v: k for k, v in self.allergy_dict.items()}
        
        for n in allergy_set:
            for s in n:
                if s in self.allergy_list and inv_allergy.get(s):
                    answer_list.append(inv_allergy.get(s)) 
           
        return list(answer_list)

