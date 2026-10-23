class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        low, high = 0, m
        while low <= high: 
            mid = low + (high - low) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target: 
                m = mid
                break
            elif matrix[mid][0] > target: 
                high = mid - 1
            elif matrix[mid][-1] < target: 
                low = mid + 1
            else: 
                return False
        n = len(matrix[m]) - 1
        low, high = 0, n
        while low <= high: 
            mid = low + (high - low) // 2
            if matrix[m][mid] == target: 
                return True
            elif matrix[m][mid] > target: 
                high = mid - 1
            elif matrix[m][mid] < target: 
                low = mid + 1
        return False

