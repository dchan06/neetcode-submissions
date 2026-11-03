class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        max_length = 0 
        l = 0
        for r in range(len(s)): 
            while s[r] in uniq: 
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            max_length=max(len(uniq), max_length)
        return max_length
        