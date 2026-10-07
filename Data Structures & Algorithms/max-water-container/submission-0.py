class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        b_area = 0
        while l < r: 
            base = r - l
            height = min(heights[l], heights[r])
            area = height * base
            if area > b_area: 
                b_area = area
            if heights[r] >= heights[l]: 
                l += 1
            else: 
                r -= 1
        return b_area
            