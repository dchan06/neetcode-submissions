from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        k = 0 
        while lo <= hi: 
            mid = lo + (hi - lo) // 2
            hrs = 0 
            for p in piles: 
                hrs += ceil(p / mid)
            if hrs <= h: 
                k = mid
                hi = mid - 1
            elif hrs > h: 
                lo = mid + 1
        return k 
