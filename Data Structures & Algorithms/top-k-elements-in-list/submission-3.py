import random

class Solution:
    def sort(self, l: List[int]): 
        if len(l) <= 1:
            return l
        pivot_index = random.randint(0,len(l)-1)
        pivot = l[pivot_index]
        l.remove(pivot)
        smaller = []
        bigger = []
        for item in l:
            if item <= pivot: 
                smaller.append(item)
            elif item > pivot: 
                bigger.append(item)
        return self.sort(bigger) + [pivot] + self.sort(smaller) 

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        count_list = list(count.values())
        sorted_list = self.sort(count_list)
        target = sorted_list[:k]
        output = []
        for key in count: 
            if count[key] in target:
                output.append(key)
        return output
        
            
            

