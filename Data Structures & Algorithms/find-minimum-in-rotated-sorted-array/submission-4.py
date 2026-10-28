class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        curr = 0
        while lo <= hi: 
            mid = lo + ((hi - lo) // 2)
            curr = nums[mid]
            if nums[mid] >= nums[hi]: 
                lo = mid + 1
            else:
                hi = mid
        return curr
            