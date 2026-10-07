class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = []
        for i, a in enumerate(nums): 
            if a > 0: 
                break
            if i > 0 and a == nums[i - 1]: 
                continue
            l, r = i + 1, len(nums) - 1 
            while l < r: 
                if nums[l] == nums[l - 1] and l-1 > i: 
                        l += 1
                        continue
                if -(nums[l] + nums[r]) == a:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif -(nums[l] + nums[r]) < a: 
                    r -= 1
                else: 
                    l += 1
        return res
            
                    