class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest_area = 0
        stk = []  # [starting index, height]
        for i, h in enumerate(heights): 
            popped_ind = i
            while stk and stk[-1][1] > h:
                popped_ind, popped_h = stk.pop()
                largest_area = max(largest_area,(i - popped_ind) * popped_h)
            curr_area = 1 * h
            if curr_area > largest_area: 
                largest_area = curr_area
            stk.append([popped_ind, h])
        for (i, h) in stk: 
            largest_area = max(largest_area,(len(heights) - i) * h)
        return largest_area
            