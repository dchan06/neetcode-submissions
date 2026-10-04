class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_seen = [set() for _ in range(9)]
        cols_seen = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for r in range(9): 
            for c in range(9): 
                item = board[r][c] 
                if item == ".":
                    continue
                box = (r // 3) * 3 + (c // 3)
                if item in rows_seen[r] or item in cols_seen[c] or item in boxes[box]: 
                    return False
                rows_seen[r].add(item)
                cols_seen[c].add(item)
                boxes[box].add(item)
        return True