class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([char for char in s if char.isalnum()]).lower()
        s_reversed = new_s[::-1]
        if new_s == s_reversed: 
            return True
        return False
