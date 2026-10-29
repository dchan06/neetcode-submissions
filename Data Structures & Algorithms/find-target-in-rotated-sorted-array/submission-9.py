class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        while lo <= hi: 
            mid = lo + ((hi - lo) // 2)
            if target == nums[mid]: 
                return mid
            elif nums[mid] >= nums[hi]: 
                if target > nums[hi] and target < nums[mid]: 
                    hi = mid - 1# go left
                else: 
                    lo = mid + 1# go right
            else: 
                if target > nums[mid] and target <= nums[hi]: 
                    lo = mid + 1    # go right
                else: 
                    hi = mid -1     # go left

        return -1 
                