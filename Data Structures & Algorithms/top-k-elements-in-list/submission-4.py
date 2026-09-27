class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = defaultdict(int)
        for num in nums: 
            count[num] += 1
        for key, value in count.items(): 
            bucket[value].append(key)
        output = []
        for freq in range(len(bucket)-1,0,-1): 
            for num in bucket[freq]: 
                output.append(num)
            if len(output) >= k: 
                return output
        return output