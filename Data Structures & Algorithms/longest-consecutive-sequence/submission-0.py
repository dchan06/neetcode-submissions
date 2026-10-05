class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        longest = 0
        start = []
        num_set = set(nums)
        print(num_set)
        for n in num_set: 
            if (n-1) not in num_set: 
                count += 1
                while (n+1) in num_set:
                    count += 1
                    n += 1
            if count > longest: 
                longest = count
            count = 0
        return longest